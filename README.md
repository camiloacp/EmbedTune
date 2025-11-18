# 🎧 EmbedTune

Sistema inteligente de recomendación musical basado en embeddings y aprendizaje automático, con una interfaz moderna inspirada en Spotify.

## 📋 Descripción

EmbedTune es una aplicación de recomendación de canciones que utiliza **Word2Vec** y **embeddings** para encontrar música similar basándose en patrones de playlists. El sistema analiza la co-ocurrencia de canciones en playlists para generar recomendaciones personalizadas y precisas.

## ✨ Características

- 🎵 **Búsqueda inteligente** de canciones con autocompletado
- 🤖 **Recomendaciones basadas en IA** utilizando modelos de embeddings
- 🎨 **Interfaz moderna** con diseño inspirado en Spotify
- 📊 **Múltiples modos de visualización** (cards, tabla, o ambos)
- ⭐ **Sistema de favoritos** para guardar canciones
- 📜 **Historial de búsquedas** recientes
- 📥 **Exportación de resultados** en CSV y TXT
- ⚙️ **Configuración personalizable** del número de recomendaciones

## 🛠️ Tecnologías

- **PyTorch** - Framework de deep learning
- **Transformers & Sentence-Transformers** - Modelos de lenguaje
- **Gensim** - Implementación de Word2Vec
- **Streamlit** - Interfaz de usuario interactiva
- **Spotipy** - API de Spotify
- **Pandas & NumPy** - Procesamiento de datos
- **scikit-learn** - Machine learning utilities

## 📦 Instalación

### Requisitos previos

- Python >= 3.13
- pip o uv (gestor de paquetes)

### Pasos de instalación

1. **Clonar el repositorio**

```bash
git clone https://github.com/camiloacp/Spotify-EmbedRecomender.git
cd Spotify-EmbedRecomender
```

2. **Instalar dependencias**

Con pip:

```bash
pip install -r requirements.txt
```

Con uv:

```bash
uv sync
```

3. **Configurar variables de entorno** (opcional)

Crear un archivo `.env` en la raíz del proyecto con tus credenciales de Spotify:

```env
SPOTIPY_CLIENT_ID=tu_client_id
SPOTIPY_CLIENT_SECRET=tu_client_secret
```

## 🚀 Uso

### Ejecutar la aplicación web

```bash
streamlit run app/app.py
```

La aplicación se abrirá automáticamente en `http://localhost:8501`

### Usar desde Python

```python
from app.recommendations import print_recommendations

# Obtener recomendaciones por nombre de canción
print_recommendations("Bohemian Rhapsody", top_n=10)

# Obtener recomendaciones por token
print_recommendations(1234, top_n=5)
```

## 📁 Estructura del Proyecto

```
EmbedTune/
├── app/
│   ├── app.py                  # Aplicación principal Streamlit
│   ├── recommendations.py      # Sistema de recomendaciones
│   ├── modelo.py              # Gestión del modelo ML
│   ├── data_extractor.py      # Extracción de datos de Spotify
│   ├── tokenizer_songs.py     # Tokenización de canciones
│   ├── autentication.py       # Autenticación Spotify API
│   └── utils.py               # Utilidades generales
├── data/
│   ├── canciones_playlists_generos.csv  # Dataset de canciones
│   └── datos_tokenizacion.pkl           # Datos tokenizados
├── model/
│   └── modelo.pkl             # Modelo Word2Vec entrenado
├── Embeddings.ipynb           # Notebook de experimentación
├── requirements.txt           # Dependencias del proyecto
├── pyproject.toml            # Configuración del proyecto
└── README.md                 # Este archivo
```

## 🎯 Cómo Funciona

1. **Tokenización**: Las canciones se convierten en tokens únicos
2. **Entrenamiento**: Se entrena un modelo Word2Vec con playlists tokenizadas
3. **Embeddings**: Cada canción obtiene una representación vectorial
4. **Similitud**: Se calculan canciones similares usando similitud coseno
5. **Recomendaciones**: Se devuelven las N canciones más similares

## 🎮 Funcionalidades de la Interfaz

### Barra Lateral

- ⚙️ Configuración del número de recomendaciones (5-20)
- 🎨 Selector de modo de visualización
- 📜 Historial de búsquedas recientes
- ⭐ Canciones favoritas guardadas

### Página Principal

- 🔍 Buscador de canciones con sugerencias
- 🎵 Recomendaciones personalizadas
- 💚 Sistema de favoritos por canción
- 📥 Exportación de resultados
- ⭐ Sistema de calificación

## 📊 Dataset

El proyecto utiliza un dataset de canciones extraídas de playlists de Spotify, que incluye:

- Nombres de canciones
- Artistas
- Géneros musicales
- Relaciones entre canciones en playlists

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👨‍💻 Autor

Desarrollado con 💚 por el equipo de EmbedTune

## 🔮 Roadmap

- [ ] Integración completa con Spotify API para reproducción
- [ ] Sistema de autenticación de usuarios
- [ ] Análisis de audio features (tempo, energy, valence)
- [ ] Recomendaciones basadas en estado de ánimo
- [ ] Playlist generator automático
- [ ] API REST para integraciones externas

## 📧 Contacto

Para preguntas o sugerencias, por favor abre un issue en el repositorio.

---

**Nota**: Este proyecto es con fines educativos y de investigación. No está afiliado oficialmente con Spotify.
