#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);  // Dirección del LCD (0x27) y tamaño (16x2)

String partidos[7][2];  // 7 partidos en total (cuartos, semifinales, final)
int goles[7][2];        // Matriz para almacenar los goles de los 7 partidos
int partidoActual = 0;  // Índice del partido actual

// Pines de los botones
const int botonAvanzarPin = 2;    // Botón para avanzar entre partidos
const int botonGolEquipo1Pin = 3; // Botón para sumar gol al equipo 1
const int botonGolEquipo2Pin = 4; // Botón para sumar gol al equipo 2

// Variables para evitar rebotes en los botones
bool botonAvanzarPresionado = false;
bool botonGolEquipo1Presionado = false;
bool botonGolEquipo2Presionado = false;

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Esperando datos...");

  Serial.begin(9600);

  // Configuración de pines de los botones
  pinMode(botonAvanzarPin, INPUT_PULLUP);
  pinMode(botonGolEquipo1Pin, INPUT_PULLUP);
  pinMode(botonGolEquipo2Pin, INPUT_PULLUP);
}

void loop() {
  // Leer datos del puerto serie
  if (Serial.available()) {
    String linea = Serial.readStringUntil('\n');
    linea.trim();
    Serial.println("Datos recibidos: " + linea);  // Para ver los datos que recibe Arduino
    if (linea.startsWith("partidos:")) {
      recibirPartidos(linea.substring(9));  // Recibir los partidos y procesarlos
      mostrarPartidoActual();
    }
  }

  // Botón para avanzar entre partidos
  if (digitalRead(botonAvanzarPin) == LOW && !botonAvanzarPresionado) {
    botonAvanzarPresionado = true;
    avanzarPartido();
  } else if (digitalRead(botonAvanzarPin) == HIGH) {
    botonAvanzarPresionado = false;
  }

  // Botón para sumar gol al equipo 1
  if (digitalRead(botonGolEquipo1Pin) == LOW && !botonGolEquipo1Presionado) {
    botonGolEquipo1Presionado = true;
    sumarGol(0);
  } else if (digitalRead(botonGolEquipo1Pin) == HIGH) {
    botonGolEquipo1Presionado = false;
  }

  // Botón para sumar gol al equipo 2
  if (digitalRead(botonGolEquipo2Pin) == LOW && !botonGolEquipo2Presionado) {
    botonGolEquipo2Presionado = true;
    sumarGol(1);
  } else if (digitalRead(botonGolEquipo2Pin) == HIGH) {
    botonGolEquipo2Presionado = false;
  }
}

// Función para recibir los partidos y sus datos
void recibirPartidos(String datos) {
  for (int i = 0; i < 7; i++) {  // Solo 7 partidos
    partidos[i][0] = "";
    partidos[i][1] = "";
    goles[i][0] = 0;  // Reinicia los goles para el equipo 1
    goles[i][1] = 0;  // Reinicia los goles para el equipo 2
  }
  partidoActual = 0;

  int partidoIndex = 0;
  while (datos.length() > 0 && partidoIndex < 7) {  // Solo 7 partidos
    int comaIndex = datos.indexOf(',');
    int puntoYComaIndex = datos.indexOf(';');

    if (comaIndex != -1 && puntoYComaIndex != -1) {
      String equipo1 = datos.substring(0, comaIndex);
      String equipo2 = datos.substring(comaIndex + 1, puntoYComaIndex);

      // Verificar que los equipos no sean vacíos antes de asignarlos
      if (equipo1.length() > 0 && equipo2.length() > 0) {
        partidos[partidoIndex][0] = equipo1;
        partidos[partidoIndex][1] = equipo2;
        Serial.println("Partido recibido: " + equipo1 + " vs " + equipo2);  // Imprimir los equipos recibidos
      }

      datos = datos.substring(puntoYComaIndex + 1);
      partidoIndex++;
    } else {
      break;  // Si no encontramos coma y punto y coma, salimos
    }
  }
  // Mostrar los partidos después de recibir todos los datos
  mostrarPartidoActual();
}

// Función para mostrar el partido actual en el LCD
void mostrarPartidoActual() {
  if (partidoActual < 7) {  // Solo hasta 7 partidos
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Partido: ");
    lcd.print(partidos[partidoActual][0]);
    lcd.print(" vs ");
    lcd.print(partidos[partidoActual][1]);

    lcd.setCursor(0, 1);
    lcd.print("G1: ");
    lcd.print(goles[partidoActual][0]);
    lcd.print(" G2: ");
    lcd.print(goles[partidoActual][1]);
  } else {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Fin torneo");
  }
}

// Función para avanzar al siguiente partido
void avanzarPartido() {
  if (partidoActual < 7) {  // Solo hasta 7 partidos
    // Determinar el ganador antes de avanzar
    determinarGanador();

    partidoActual++;
    if (partidoActual == 4) {
      // Cuando llegamos al partido 4, mostramos semifinales
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Semifinales");
      delay(2000);
    } else if (partidoActual == 6) {
      // Cuando llegamos al partido 6, mostramos la final
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Final");
      delay(2000);
    } else if (partidoActual >= 7) {  // Fin del torneo
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Torneo finalizado");
    } else {
      mostrarPartidoActual();
    }
  }
}

// Función para sumar un gol a un equipo
void sumarGol(int equipo) {
  if (partidoActual < 7) {  // Solo hasta 7 partidos
    goles[partidoActual][equipo]++;
    mostrarPartidoActual();
  }
}

// Función para determinar al ganador y enviarlo al puerto serie
void determinarGanador() {
  if (goles[partidoActual][0] > goles[partidoActual][1]) {
    // Enviar el resultado completo al puerto serie
    Serial.println("resultado:" + partidos[partidoActual][0] + " " + String(goles[partidoActual][0]) + "-" + String(goles[partidoActual][1]) + " " + partidos[partidoActual][1]);
  } else if (goles[partidoActual][1] > goles[partidoActual][0]) {
    // Enviar el resultado completo al puerto serie
    Serial.println("resultado:" + partidos[partidoActual][1] + " " + String(goles[partidoActual][1]) + "-" + String(goles[partidoActual][0]) + " " + partidos[partidoActual][0]);
  } else {
    // Enviar el empate
    Serial.println("resultado:Empate " + partidos[partidoActual][0] + " " + String(goles[partidoActual][0]) + "-" + String(goles[partidoActual][1]) + " " + partidos[partidoActual][1]);
  }
}


