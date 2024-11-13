#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

int botonGolEquipo1 = 2;
int botonGolEquipo2 = 3;
int botonGuardar = 4;

int golesEquipo1 = 0;
int golesEquipo2 = 0;

void setup() {
  lcd.begin();
  lcd.backlight();
  
  pinMode(botonGolEquipo1, INPUT_PULLUP);
  pinMode(botonGolEquipo2, INPUT_PULLUP);
  pinMode(botonGuardar, INPUT_PULLUP);
  
  mostrarPartido("Equipo 1", "Equipo 2");
}

void loop() {
  if (digitalRead(botonGolEquipo1) == LOW) {
    golesEquipo1++;
    actualizarDisplay();
    delay(200); // Anti-rebote
  }
  
  if (digitalRead(botonGolEquipo2) == LOW) {
    golesEquipo2++;
    actualizarDisplay();
    delay(200); // Anti-rebote
  }
  
  if (digitalRead(botonGuardar) == LOW) {
    enviarResultado();
    delay(200); // Anti-rebote
  }
}

void mostrarPartido(String equipo1, String equipo2) {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(equipo1);
  lcd.setCursor(0, 1);
  lcd.print(equipo2);
  actualizarDisplay();
}

void actualizarDisplay() {
  lcd.setCursor(10, 0);
  lcd.print(golesEquipo1);
  lcd.setCursor(10, 1);
  lcd.print(golesEquipo2);
}

void enviarResultado() {
  // Enviar los goles al sistema Qt para determinar el ganador.
  golesEquipo1 = 0;
  golesEquipo2 = 0;
  actualizarDisplay();
}
