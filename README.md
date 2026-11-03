# 🗄️ CREAR E IMPORTAR UNA BASE DE DATOS MYSQL
### ⚙️ Laragon 6 | MySQL / MariaDB | Windows

---

## 🎯 OBJETIVO

Documentar el procedimiento para crear una base de datos, importar un archivo `.sql` y verificar la cantidad de registros de cada tabla.

## 🟢 PASO 1. ABRIR LA TERMINAL DE LARAGON

1. Abrir **Laragon 6**.
2. Iniciar los servicios de MySQL.
3. Abrir la terminal de Laragon.

Ingresar a MySQL:

```bash
mysql -u root -p
```

> 💡 En una instalación predeterminada de Laragon, el usuario `root` normalmente no tiene contraseña. Cuando aparezca `Enter password:`, presionar ENTER.

---

## 🟢 PASO 2. CREAR LA BASE DE DATOS

Dentro de MySQL, ejecutar:

```sql
CREATE DATABASE octubre2;
```

Seleccionar la base de datos:

```sql
USE octubre2;
```

Salir de MySQL:

```sql
exit;
```

### 📖 Explicación

| Comando | Función |
|---|---|
| `CREATE DATABASE` | Crea una nueva base de datos. |
| `USE` | Selecciona la base de datos. |
| `exit` | Sale de MySQL. |

---

## 🟢 PASO 3. IMPORTAR EL ARCHIVO SQL

Desde la terminal de Laragon (fuera de MySQL), ejecutar:

```bash
mysql -u root -p octubre2 < "C:\Users\GOKU\Desktop\recupera\octubre2.sql"
```

### 🔍 Descripción del comando

| Elemento | Función |
|---|---|
| `mysql` | Ejecuta el cliente MySQL. |
| `-u root` | Usuario de conexión. |
| `-p` | Solicita contraseña. |
| `octubre2` | Base de datos de destino. |
| `<` | Redirige el archivo SQL hacia MySQL. |
| Ruta `.sql` | Ubicación del respaldo. |

> ⚠️ **IMPORTANTE:** Si la contraseña está vacía, presionar ENTER cuando aparezca `Enter password:`. Si la importación termina correctamente, normalmente regresarás al terminal sin mostrar mensajes.

---

## 🟢 PASO 4. VERIFICAR LAS TABLAS IMPORTADAS

Ingresar nuevamente a MySQL:

```bash
mysql -u root -p
```

Seleccionar la base de datos:

```sql
USE octubre2;
```

Mostrar todas las tablas:

```sql
SHOW TABLES;
```

<details>
<summary>📌 ¿Qué debemos verificar?</summary>

Que aparezcan las tablas correspondientes al respaldo importado.

</details>

---

## 🟢 PASO 5. CONSULTAR LA CANTIDAD DE REGISTROS


### MÉTODO  CONSULTAS PARA CONTEOS EXACTOS

Para obtener el número real de registros de cada tabla, utilizaremos `COUNT(*)`.

Ejecutar:

```sql
SELECT CONCAT(
    'SELECT "', TABLE_NAME, '" AS tabla, COUNT(*) AS registros FROM `',
    TABLE_NAME, '` UNION ALL '
)
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'octubre2'
AND TABLE_TYPE = 'BASE TABLE';
```

### ⚙️ ¿Qué hace esta consulta?

Genera automáticamente una consulta SQL para cada tabla de la base de datos.

**Ejemplo del resultado generado:**

```sql
SELECT "t_clientes" AS tabla, COUNT(*) AS registros FROM `t_clientes` UNION ALL
SELECT "t_productos" AS tabla, COUNT(*) AS registros FROM `t_productos` UNION ALL
SELECT "t_ventas" AS tabla, COUNT(*) AS registros FROM `t_ventas` UNION ALL
```
vendrá con | | que hay que quitarlo y elimiar UNION ALL del ultimo dato y poner un ;

### 📌 IMPORTANTE: EJECUTAR EL RESULTADO GENERADO

1. Copiar todas las consultas generadas.
2. Pegarlas nuevamente en MySQL.
3. Eliminar el último `UNION ALL`.
4. Ejecutar el conjunto de consultas.

**Resultado esperado:**

| tabla | registros |
|---|---:|
| t_clientes | 150 |
| t_productos | 320 |
| t_ventas | 85 |

> ✅ Este segundo método utiliza `COUNT(*)` para obtener cantidades exactas, no estimadas.

*Los nombres y cantidades de la tabla son ejemplos ilustrativos. *

---

## 📋 RESUMEN DE COMANDOS

| Operación | Comando |
|---|---|
| Entrar a MySQL | `mysql -u root -p` |
| Crear base de datos | `CREATE DATABASE octubre2;` |
| Seleccionar base de datos | `USE octubre2;` |
| Salir de MySQL | `exit;` |
| Importar respaldo | `mysql -u root -p octubre2 < "RUTA"` |
| Mostrar tablas | `SHOW TABLES;` |
| Consultar registros estimados | `TABLE_ROWS` |
| Consultar registros exactos | `COUNT(*)` |

---



**📚 DOCUMENTACIÓN TÉCNICA PERSONAL**

*Procedimiento probado para creación, importación y verificación de bases de datos MySQL mediante Laragon 6.*
