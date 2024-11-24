#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Definir el LCD en el puerto I2C (dirección 0x3F para el LCD de 16x2)
LiquidCrystal_I2C lcd(0x3F, 16, 2);

// Variables para almacenar los goles
int golesEquipo1 = 0;
int golesEquipo2 = 0;

int botonGol1 = 2; // Botón para goles del equipo 1
int botonGol2 = 3; // Botón para goles del equipo 2
int botonResultado = 4; // Botón para pasar el resultado

// Variables para almacenar los nombres de los equipos
String equipo1 = "Equipo 1";
String equipo2 = "Equipo 2";

// Declaración de funciones
void mostrarMensaje(String mensaje);
void actualizarPantalla(String equipo1, String equipo2, int goles1, int goles2);

void setup() {
  // Inicializa el LCD y los botones
  lcd.begin(16, 2);
  lcd.backlight();
  
  pinMode(botonGol1, INPUT);
  pinMode(botonGol2, INPUT);
  pinMode(botonResultado, INPUT);

  // Mostrar mensaje inicial
  mostrarMensaje("Torneo de Futbol");
  delay(2000);
  actualizarPantalla(equipo1, equipo2, golesEquipo1, golesEquipo2);
}

void loop() {
  // Detectar si se presiona algún botón
  if (digitalRead(botonGol1) == HIGH) {
    golesEquipo1++; // Sumar gol al equipo 1
    actualizarPantalla(equipo1, equipo2, golesEquipo1, golesEquipo2);
    delay(500); // Retardo para evitar rebote
  }
  
  if (digitalRead(botonGol2) == HIGH) {
    golesEquipo2++; // Sumar gol al equipo 2
    actualizarPantalla(equipo1, equipo2, golesEquipo1, golesEquipo2);
    delay(500); // Retardo para evitar rebote
  }
  
  if (digitalRead(botonResultado) == HIGH) {
    mostrarMensaje("Esperando Resultados...");
    // Lógica para verificar el ganador
    if (golesEquipo1 > golesEquipo2) {
      mostrarMensaje(equipo1 + " Gana!");
    } else if (golesEquipo2 > golesEquipo1) {
      mostrarMensaje(equipo2 + " Gana!");
    } else {
      mostrarMensaje("Empate!");
    }
    delay(2000); // Mostrar resultado
    golesEquipo1 = 0; // Reiniciar goles
    golesEquipo2 = 0; // Reiniciar goles
    actualizarPantalla(equipo1, equipo2, golesEquipo1, golesEquipo2); // Actualizar pantalla
  }
}

// Función para mostrar mensajes en el LCD
void mostrarMensaje(String mensaje) {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(mensaje);
  delay(2000); // Tiempo para que el mensaje sea visible
}

// Función para actualizar la pantalla con los nombres de los equipos y goles
void actualizarPantalla(String equipo1, String equipo2, int goles1, int goles2) {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(equipo1 + " " + String(goles1)); // Mostrar equipo 1 y goles
  lcd.setCursor(0, 1);
  lcd.print(equipo2 + " " + String(goles2)); // Mostrar equipo 2 y goles
}


