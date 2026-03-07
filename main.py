from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen


class MainScreen(MDScreen):
    
    # On crée la fonction pour afficher le texte dans le terminal
    def clickButton(self):
        
        print("Bonjour, Le bouton fonctionne")
        
    def otherButton(self):
        
        print("Le deuxième bouton fonctionne !!!")
        
        
class MainApp(MDApp):
    
    def build(self):
        
        # On choisi un thème de couleur
        self.theme_cls.primary_palette = "Orange"
        
        # On choisi un style
        self.theme_cls.theme_style = "Light"  # ou Dark
        
        # on renvois l'écran
        return MainScreen()
    
    def changeStyle(self):
        
        style = self.theme_cls.theme_style
        
        self.theme_cls.theme_style = "Light" if style == "Dark" else "Dark"
        
        
if __name__ == "__main__":
    
    # On lance notre programme
    MainApp().run()
