import os
from typing import List
from bbas import bbas

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

@staticmethod
class Framework:
    def __init__(self):
        self._framework = None
        self.bbas = bbas()

    def set_framework_mode(self, framework):
        self._framework = framework

    def get_framework(self):
        return self._framework
    
    def set_bbas(self, subpath):
        # A MODIFIER POUR PLUSIEURS TESTS ! 'datasets/PHM'
        directory_path = 'datasets' + '/' + subpath

        combined_bbas = load_all_bbas_from_directory(directory_path)
        self.bbas = combined_bbas
    
    def get_bbas(self):
        # Check if BBAs are set or imagine transformation/checks
        if self.bbas is None:
            raise ValueError("No BBAs have been set yet.")
        
        self.bbas.display()

    
    def CWAC(self, dissimilarity_matrix):
        bbas = self.get_bbas()
        combined_bba = []



        return combined_bba
    
    def calculate_betp(self, bba):
        betp = bba / np.sum(bba, axis=1, keepdims=True)
        
        return betp
    
