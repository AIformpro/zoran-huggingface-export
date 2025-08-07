"""
export_model.py: Script pour publier un modèle ou jeu de données Zoran sur HuggingFace Hub.

Ce script utilise la bibliothèque huggingface_hub pour authentifier l'utilisateur et créer
un dépôt distant, puis y pousser les fichiers du modèle ou du dataset.
"""

import argparse
from pathlib import Path
from huggingface_hub import HfApi, upload_folder


def main():
    parser = argparse.ArgumentParser(description="Publier un modèle ou dataset Zoran sur le HuggingFace Hub.")
    parser.add_argument("--token", required=True, help="Jeton d'authentification HuggingFace.")
    parser.add_argument("--repo_name", required=True, help="Nom du dépôt sur le Hub, par ex. username/zoran-model.")
    parser.add_argument("--local_path", default="models", help="Chemin local vers le dossier à exporter (models ou datasets).")
    args = parser.parse_args()

    api = HfApi()
    api.set_access_token(args.token)
    folder_path = Path(args.local_path)
    if not folder_path.exists():
        raise FileNotFoundError(f"Dossier {folder_path} introuvable")

    print(f"Export du contenu de {folder_path} vers {args.repo_name}...")
    upload_folder(folder_path=folder_path, repo_id=args.repo_name, repo_type='model', token=args.token)
    print("Export terminé.")


if __name__ == '__main__':
    main()
