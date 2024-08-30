import json
import os
from typing import List

class bbas:
    def __init__(self):
        self.bbas: List[List[float]] = []  # Liste pour stocker les bbas de chaque source
    
    def add_bba(self, bba: List[float]):
        """
        Ajouter un BBA à la liste.
        
        Parameters:
        - bba (List[float]): BBA pour une source d'information.
        """
        self.bbas.append(bba)
    
    def load_from_file(self, file_path: str):
        """
        Charger les bbas à partir d'un fichier JSON et les ajouter à la liste.
        
        Parameters:
        - file_path (str): Chemin du fichier JSON contenant les bbas.
        """
        with open(file_path, 'r') as f:
            bba_data = json.load(f)
            for key in bba_data:
                self.add_bba(bba_data[key])
    
    def display(self):
        """
        Afficher les bbas stockés.
        """
        print(f"Total number of bbas loaded: {len(self.bbas)}")
        for idx, bba in enumerate(self.bbas):
            print(f"BBA {idx + 1}: {bba}")

def load_all_bbas_from_directory(directory_path: str) -> bbas:
    """
    Charger tous les fichiers bbas JSON d'un dossier spécifié dans un objet bbas.
    
    Parameters:
    - directory_path (str): Chemin du dossier contenant les fichiers JSON.
    
    Returns:
    - bbas: Objet bbas contenant toutes les sources d'information.
    """
    bbas_object = bbas()
    
    # Parcourir tous les fichiers du dossier
    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):  # Vérifier que le fichier est bien un fichier JSON
            file_path = os.path.join(directory_path, filename)
            bbas_object.load_from_file(file_path)
    
    return bbas_object


