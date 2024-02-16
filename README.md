# GH DevOps bootcamp final project

El objetivo de este proyecto final de Bootcamp DevOps es automatizar el ciclo de vida de una aplicación web, abarcando desde su desarrollo hasta su despliegue y monitorización. Este proceso incluye la contenedorización de la aplicación para asegurar su portabilidad y facilidad de despliegue, la integración y despliegue continuo para facilitar la entrega de cambios de manera eficiente, y la orquestación de contenedores para gestionar su escalado y operación en entornos de producción. La monitorización proporciona visibilidad sobre el rendimiento de la aplicación y la infraestructura subyacente, permitiendo una respuesta rápida a cualquier problema. Con este enfoque se mejora la agilidad, la eficiencia en el desarrollo y despliegue de aplicaciones y asegura la alta disponibilidad y la escalabilidad en entornos de producción.

### Tecnologías y Diseño de la Arquitectura

- **Docker**: Se utilizará para contenerizar la aplicación web y sus dependencias, asegurando la consistencia del entorno de ejecución desde el desarrollo hasta la producción.
- **GitHub Actions**: Automatizará el flujo de trabajo de CI/CD, permitiendo la construcción y prueba de la aplicación directamente desde GitHub cada vez que se realice un commit y así automatizar la construcción de imágenes, ejecución de pruebas, y el despliegue en diferentes ambientes.
- **Kubernetes**: Orquestará el despliegue, la escalabilidad, y la gestión de los contenedores de la aplicación con la definición de manifiestos para definir los pods, servicios, volúmenes, y otras configuraciones necesarias.
- **Grafana**: Se empleará para la monitorización de la aplicación y la infraestructura.

- T**erraform**: Para definir y aprovisionar la infraestructura necesaria en la nube de forma automática y reproducible. Esto incluirá recursos como clusters de Kubernetes, servicios de bases de datos, y almacenamiento.

- **GitHub Actions**: Para definir pipeline de CI/CD que incluirá etapas para la validación del código, construcción y prueba de la imagen de Docker, y despliegue automático a Kubernetes.

### Descripción del proyecto

El proyecto que se presenta es una siple API de gestion de ToDo de forma colaborativa donde varios integrantes pudieran planificarse las suyas. La estructura consta de la tarea que se quiera realizar y su estatus como completado o no. En la base de datos, pues, se almacena esta información con un identificador único corresopndiente al usuario que la crreo y otro con respecto a todos los identificadores de la tabla. 
```json
{
    "title": "delectus aut autem",
    "completed": false
}
```

---
> ...en construcctión  👨‍💻 🏗️ 🛜 😓