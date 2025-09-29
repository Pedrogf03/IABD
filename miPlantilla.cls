\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{miPlantilla}[2025/09/25 Clase personalizada basada en article]

% Basada en article con tamaño 12pt y A4
\LoadClass[12pt,a4paper]{article}

% --------------------
% Paquetes necesarios
% --------------------
\RequirePackage[spanish]{babel}
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{fancyhdr}
\RequirePackage{hyperref}
\RequirePackage{graphicx}
\RequirePackage[a4paper, top=2cm, bottom=2cm]{geometry}
\RequirePackage{float}
\RequirePackage{subfigure}
\RequirePackage{url}

% Configuración de hyperref
\hypersetup{
    colorlinks=true,
    linkcolor=black,
    urlcolor=blue,
    citecolor=blue
}

% --------------------
% Ajustes generales
% --------------------
\setlength{\textfloatsep}{10pt plus 1pt minus 2pt}   % Espacio entre texto y figuras
\setlength{\parindent}{0pt}   % Sin sangría
\setlength{\parskip}{0.5em}   % Espacio entre párrafos

\usepackage{sectsty}           % Cambiar tamaño de títulos
\sectionfont{\large}           
\subsectionfont{\normalsize}  
\subsubsectionfont{\small}    

\setlength{\headheight}{15pt}  % Para fancyhdr

% --------------------
% Comandos personalizados
% --------------------
\newcommand{\miNombre}{Pedro González Fernández} % fijo
\newcommand{\miAsignatura}{}  % lo cambias según el documento
\newcommand{\tituloTrabajo}{} % lo cambias según el documento
\newcommand{\imagenPortada}{} % ruta de la imagen de portada

% --------------------
% Configuración de encabezado/pie
% --------------------
\pagestyle{fancy}
\fancyhf{} % limpiar encabezados y pies
\fancyhead[L]{\miNombre}
\fancyhead[R]{\miAsignatura}
\fancyfoot[C]{\thepage}

% --------------------
% Definición de portada personalizada
% --------------------
\renewcommand{\maketitle}{%
    \begin{titlepage}
        \centering
        \vspace*{\fill} % centra verticalmente desde arriba
        
        {\Huge \tituloTrabajo \par} % título grande
        \vspace{1cm}
        
        {\Large \miNombre \par} % nombre más pequeño
        \vspace{1cm}
        
        % Imagen de portada si se ha definido
        \ifx\imagenPortada\empty
        % no mostrar nada si está vacío
        \else
            \includegraphics[width=1\textwidth]{\imagenPortada}\par
            \vspace{1cm}
        \fi
        
        {\small \today \par} % fecha más pequeña
        
        \vspace*{\fill} % centra verticalmente hasta abajo
    \end{titlepage}
    
    \newpage
    \vspace*{\fill}      % relleno arriba
    \begin{center}       % centra horizontalmente
        \tableofcontents
    \end{center}
    \vspace*{\fill}      % relleno abajo
    \newpage
}

% --------------------
% Comando para figuras simplificado
% --------------------
\newcommand{\fig}[2][0.7\textwidth]{
    \begin{figure}[H]
        \centering
        \includegraphics[width=#1]{#2}
    \end{figure}
}

