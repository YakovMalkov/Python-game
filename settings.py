class Settings():
     """Класс для хранения всех настроек игры Alien Invasion."""
     def __init__(self):
          """Инициализирует настройки игры."""
          # Параметры экрана
          self.screen_width = 1200
          self.screen_height = 800
          self.bg_color = (91, 119, 172)

          # Настройки корабля
          self.ship_speed = 0.8

          # Параметры снаряда
          self.bullet_speed = 1.5
          self.bullet_width = 7
          self.bullet_height = 19
          self.bullet_color = (225, 195, 28)
          self.bullets_allowed = 15

          # Настройки пришельцев
          self.alien_speed = 1.0
          self.fleet_drop_speed = 10
          # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
          self.fleet_direction = 1
