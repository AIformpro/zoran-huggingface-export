# zoran-huggingface-export

Ce dépôt contient les scripts et documents nécessaires pour exporter les composants mimétiques Zoran (modèles et jeux de données) vers la plateforme HuggingFace.

## Contenu
- `export_model.py` : script Python pour publier un modèle Zoran sur le Hub HuggingFace.
- `datasets/` : répertoire pour les jeux de données glottaux prêts à être poussés sur le Hub.
- `models/` : répertoire pour les poids de modèles et configurations.
- `README.md` : ce fichier d'introduction.
- `.gitignore` : fichiers ignorés.
- `LICENSE` : licence MIT.

## Utilisation
1. Installez les dépendances nécessaires (huggingface-hub).
2. Préparez votre modèle Zoran ou votre dataset.
3. Configurez vos identifiants HF (`huggingface-cli login`).
4. Exécutez `python export_model.py --token <HF_TOKEN> --repo_name <username>/<repo>` pour publier votre modèle.

## Contribuer
Les contributions, améliorations et nouveaux exports sont les bienvenus. Veuillez ouvrir une issue ou une pull request.

## Licence
Ce projet est sous licence MIT.
