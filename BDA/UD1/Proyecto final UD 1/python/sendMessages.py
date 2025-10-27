from kafka import KafkaProducer
import json, random, time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Plantas y plazas por planta
LEVELS = ["L1", "L2", "L3"]
PLAZAS_POR_PLANTA = 30

# Valores iniciales para simular variación suave
temperatura_base = {level: random.uniform(20.0, 25.0) for level in LEVELS}
bateria_base = {level: random.uniform(80.0, 100.0) for level in LEVELS}

while True:
    # Elegir planta y plaza aleatoriamente
    level = random.choice(LEVELS)
    plaza = random.randint(1, PLAZAS_POR_PLANTA)
    bay_id = f"{level}-A-{plaza}"

    # Simular cambios realistas de temperatura (±0.5 °C)
    temperatura_base[level] += random.uniform(-0.5, 0.5)
    temperatura_base[level] = max(15, min(temperatura_base[level], 35))

    # Simular drenaje de batería (disminuye lentamente con algo de ruido)
    bateria_base[level] -= random.uniform(0.0, 0.3)
    if bateria_base[level] < 10:  # recarga simulada
        bateria_base[level] = 100.0

    # Generar mensaje
    msg = {
        "bay_id": bay_id,
        "parking_id": "PK-CADIZ-01",
        "level": level,
        "occupied": random.choice([True, False]),
        "last_event_ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "metrics": {
            "temperature_c": round(temperatura_base[level], 1),
            "battery_pct": round(bateria_base[level], 1)
        },
        "updated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    }

    # Enviar mensaje a Kafka
    producer.send("smartparking.events", msg)
    print(f"Enviado: {msg}")
    time.sleep(1)
