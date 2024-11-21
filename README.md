# POO_PYTHON_2
# Martínez Estrada Ricardo / NO. de control: 1193 / 20-11-2024

Ejercicio 1. Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI.  Construye los siguientes métodos para la clase:
- Un constructor, donde los datos pueden estar vacíos.
- Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
- mostrar(): Muestra los datos de la persona.
- esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

![image](https://github.com/user-attachments/assets/1eea80c7-11e5-4f68-831d-7a52f4dcd762)
![image](https://github.com/user-attachments/assets/1280c58e-5817-4cd0-af51-fc71513625c9)
![image](https://github.com/user-attachments/assets/5309f992-27cd-4808-97ec-d1ede2989472)

-------------------------

Ejercicio 2. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
- Un constructor, donde los datos pueden estar vacíos.
- Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
- mostrar(): Muestra los datos de la cuenta.
- ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
- retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

![image](https://github.com/user-attachments/assets/88d514ab-d2a3-4bd5-a65f-1093e8b3469a)
![image](https://github.com/user-attachments/assets/32bf82c0-3495-46a1-b972-25866f31da53)
![image](https://github.com/user-attachments/assets/2088c3a5-54ba-41d4-a63d-b13ff90f7b0c)

-------------------------

Ejercicio 3. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la anterior. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento.Construye los siguientes métodos para la clase:
- Un constructor.
- Los setters y getters para el nuevo atributo.
- En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si el titular es mayor - de edad pero menor de 25 años y falso en caso contrario.
- Además la retirada de dinero sólo se podrá hacer si el titular es válido.
- El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.

![image](https://github.com/user-attachments/assets/ee4ca179-b1ff-46cb-84d0-0f78e5d71d5f)
![image](https://github.com/user-attachments/assets/0c74740d-6504-4898-b761-3560664a94cc)
![image](https://github.com/user-attachments/assets/fef63586-2600-4442-908c-d1c780fb8065)
![image](https://github.com/user-attachments/assets/d09329da-d225-4714-af96-7df669df3bea)
