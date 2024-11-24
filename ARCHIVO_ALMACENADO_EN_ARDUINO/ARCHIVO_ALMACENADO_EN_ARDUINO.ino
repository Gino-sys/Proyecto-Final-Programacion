#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define TEAM1_GOAL_PIN 2  // Botón para sumar goles al equipo 1
#define TEAM2_GOAL_PIN 3  // Botón para sumar goles al equipo 2
#define NEXT_MATCH_PIN 4  // Botón para avanzar al siguiente partido

LiquidCrystal_I2C lcd(0x27, 16, 2);

String equipos[8]; // Nombres de los equipos
int goles[2] = {0, 0}; // Goles de los equipos en el partido actual
int partidos[7][2];    // Matriz de enfrentamientos: [partido][equipo1, equipo2]
int partidoActual = 0; // Índice del partido actual
bool lastTeam1State = LOW;
bool lastTeam2State = LOW;
bool lastNextMatchState = LOW;

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();

  // Configurar botones como INPUT_PULLUP
  pinMode(TEAM1_GOAL_PIN, INPUT_PULLUP);
  pinMode(TEAM2_GOAL_PIN, INPUT_PULLUP);
  pinMode(NEXT_MATCH_PIN, INPUT_PULLUP);

  // Leer nombres de los equipos desde Python
  while (Serial.available() == 0) {
    // Esperar datos
  }
  String data = Serial.readStringUntil('\n');
  parseEquipos(data);

  // Configurar enfrentamientos de cuartos de final
  for (int i = 0; i < 4; i++) {
    partidos[i][0] = i * 2;
    partidos[i][1] = i * 2 + 1;
  }

  // Mostrar primer partido
  mostrarPartido();
}

void loop() {
  // Botón para sumar goles al equipo 1
  bool team1State = digitalRead(TEAM1_GOAL_PIN);
  if (team1State == LOW && lastTeam1State == HIGH) {
    goles[0]++;
    mostrarPartido();  // Actualizar pantalla con los nuevos goles
    delay(200); // Evitar rebotes
  }
  lastTeam1State = team1State;

  // Botón para sumar goles al equipo 2
  bool team2State = digitalRead(TEAM2_GOAL_PIN);
  if (team2State == LOW && lastTeam2State == HIGH) {
    goles[1]++;
    mostrarPartido();  // Actualizar pantalla con los nuevos goles
    delay(200); // Evitar rebotes
  }
  lastTeam2State = team2State;

  // Botón para avanzar al siguiente partido
  bool nextMatchState = digitalRead(NEXT_MATCH_PIN);
  if (nextMatchState == LOW && lastNextMatchState == HIGH) {
    avanzarPartido();
    delay(200); // Evitar rebotes
  }
  lastNextMatchState = nextMatchState;
}

void parseEquipos(String data) {
  char buffer[128];
  data.toCharArray(buffer, 128);
  char *item = strtok(buffer, ",");
  int i = 0;
  while (item != NULL && i < 8) {
    equipos[i] = String(item);
    item = strtok(NULL, ",");
    i++;
  }
}

void mostrarPartido() {
  lcd.clear();

  // Primera línea: Equipo 1 y goles
  lcd.setCursor(0, 0);
  lcd.print(equipos[partidos[partidoActual][0]]);
  lcd.print(":");
  lcd.print(goles[0]);

  // Segunda línea: Equipo 2 y goles
  lcd.setCursor(0, 1);
  lcd.print(equipos[partidos[partidoActual][1]]);
  lcd.print(":");
  lcd.print(goles[1]);
}

void avanzarPartido() {
  // Verificar si hay empate
  if (goles[0] == goles[1]) {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Empate! Repetir");
    lcd.setCursor(0, 1);
    lcd.print("partido.");
    delay(2000); // Pausa para mostrar el mensaje

    // Reiniciar goles para el partido actual
    goles[0] = 0;
    goles[1] = 0;
    mostrarPartido();  // Volver a mostrar el mismo partido
    return; // No avanzamos al siguiente partido
  }

  // Si no es empate, determinar el ganador
  int ganador = (goles[0] > goles[1]) ? partidos[partidoActual][0] : partidos[partidoActual][1];

  // Avanzar a la siguiente ronda
  if (partidoActual < 6) {
    partidos[4 + partidoActual / 2][partidoActual % 2] = ganador;
  }

  partidoActual++;
  if (partidoActual < 7) {
    // Reiniciar goles antes de mostrar el próximo partido
    goles[0] = 0;
    goles[1] = 0;
    mostrarPartido();
  } else {
    // Anunciar el ganador final
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Ganador: ");
    lcd.setCursor(0, 1);
    lcd.print(equipos[ganador]);
    Serial.println(equipos[ganador]); // Enviar ganador a Python
  }
}


