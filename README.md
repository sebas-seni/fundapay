# 💸 FundaPay - Sistema de Gestión Financiera

**FundaPay** es una aplicación de consola desarrollada en **Python** que simula el núcleo transaccional de una billetera virtual o banco digital. El sistema gestiona el ciclo de vida completo de cuentas de usuario, desde el alta hasta operaciones complejas como transferencias entre pares y liquidación de préstamos.

## 🚀 Funcionalidades Principales

El proyecto resuelve problemáticas típicas de sistemas financieros mediante una lógica robusta:

* **Gestión de Cuentas:** Alta de usuarios validada (DNI, Nombre) y manejo de saldo en tiempo real.
* **Motor Transaccional (P2P):**
    * Transferencias de dinero entre cuentas existentes.
    * Registro de auditoría (historial) en ambas partes (emisor y receptor).
    * Visualización de las últimas 5 operaciones (LIFO).
* **Módulo de Préstamos Avanzado:**
    * Otorgamiento de créditos con cálculo automático de intereses y tasas impositivas.
    * **Lógica de Amortización:** Sistema de pagos parciales con prioridad de imputación (primero se cubren impuestos, luego intereses y finalmente capital).
    * Tracking detallado de deuda pendiente vs. pagada.
* **Validaciones y Seguridad:** Sanitización de inputs, verificación de existencia de usuarios y controles de saldo negativo ("descubierto" no permitido).

## 🛠️ Tecnologías y Conceptos Aplicados

Este proyecto demuestra un dominio sólido de la manipulación de estructuras de datos complejas en memoria sin uso de bases de datos externas:

* **Estructuras de Datos Anidadas:** Uso de diccionarios de diccionarios y listas (`usuarios[dni]['prestamos'][id]`) para modelar relaciones uno-a-muchos.
* **Lógica de Negocio Financiera:** Implementación de reglas estrictas de negocio (ej: el orden de cobro en los pagos de préstamos en `logica.py`).
* **Modularización (MVC):**
    * `fundapay.py`: Entry point y orquestador.
    * `logica.py`: Reglas de negocio (cálculos, actualizaciones de estado).
    * `usuario.py` / `constantes.py`: Capa de presentación y textos.
    * `validaciones.py`: Capa de integridad de datos.
* **Algoritmos:** Filtrado y ordenamiento de historial de transacciones.

## 📋 Pre-requisitos

* Python 3.x

## 🔧 Cómo ejecutarlo

1.  Clona el repositorio.
2.  Ejecuta el archivo principal:
    ```bash
    python fundapay.py
    ```
3.  Sigue el menú interactivo para crear cuentas y operar.

## 👤 Autor
[Sebastián Senillosa / LinkedIn: www.linkedin.com/in/sebastián-senillosa-5548391a1]
