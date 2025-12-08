# 🛒 ElectroAB - Boutique High-Tech

Un site e-commerce High-Tech complet et moderne développé avec Django et Bootstrap 5. Spécialisé dans les smartphones, laptops et accessoires technologiques.

## ✨ Fonctionnalités

### 🧑‍💼 Côté Admin
- CRUD complet pour les produits
- CRUD complet pour les catégories
- Gestion des commandes
- Gestion des utilisateurs via Django Admin

### 🧑‍💻 Côté Client
- **Page d'accueil** avec produits populaires et nouveautés
- **Boutique** avec filtrage par catégorie et recherche
- **Détails produit** avec images et descriptions
- **Panier d'achat** basé sur les sessions
- **Checkout** avec formulaire de livraison
- **Paiement à la livraison**
- **Authentification** : inscription, connexion, déconnexion
- **Profil utilisateur** : mise à jour des informations
- **Historique des commandes** avec détails

## 🎨 Design

- **Palette de couleur** : Bleu #1c92cf
- **Framework CSS** : Bootstrap 5
- **Icônes** : Bootstrap Icons
- **Design** : Moderne, minimaliste, responsive

## 🚀 Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner ou télécharger le projet**

2. **Créer un environnement virtuel** (recommandé)
```bash
python -m venv venv
```

3. **Activer l'environnement virtuel**
   - Sur Windows :
   ```bash
   venv\Scripts\activate
   ```
   - Sur Linux/Mac :
   ```bash
   source venv/bin/activate
   ```

4. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

5. **Effectuer les migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Créer un superutilisateur** (pour accéder à l'admin)
```bash
python manage.py createsuperuser
```

7. **Collecter les fichiers statiques**
```bash
python manage.py collectstatic
```

8. **Lancer le serveur de développement**
```bash
python manage.py runserver
```

9. **Accéder au site**
   - Site web : http://127.0.0.1:8000/
   - Admin : http://127.0.0.1:8000/admin/

## 📁 Structure du projet

```
ecommerce/
├── core/              # Application principale (accueil, templates de base)
├── shop/              # Application boutique (produits, panier)
├── orders/            # Application commandes (checkout, gestion)
├── users/             # Application utilisateurs (authentification, profil)
├── ecommerce/         # Configuration du projet Django
├── static/            # Fichiers statiques (CSS, images)
├── media/             # Fichiers média (images produits)
├── manage.py          # Script de gestion Django
└── requirements.txt   # Dépendances Python
```

## 🗄️ Base de données

Le projet utilise SQLite par défaut (fichier `db.sqlite3`). Pour utiliser une autre base de données, modifiez `settings.py`.

## 👤 Utilisation

### Créer des produits

1. Connectez-vous à l'interface admin : http://127.0.0.1:8000/admin/
2. Allez dans **Shop > Categories** pour créer des catégories
3. Allez dans **Shop > Products** pour créer des produits
4. N'oubliez pas de cocher "Produit populaire" pour les afficher sur la page d'accueil

### Passer une commande

1. Parcourez la boutique et ajoutez des produits au panier
2. Cliquez sur l'icône panier dans la navbar
3. Vérifiez votre panier et cliquez sur "Passer la commande"
4. Remplissez le formulaire de livraison
5. Confirmez la commande (paiement à la livraison)

## 🔧 Configuration

### Modifier la palette de couleur

Pour changer la couleur principale, modifiez la variable CSS dans `static/css/style.css` :
```css
:root {
    --primary-color: #1c92cf; /* Changez cette valeur */
}
```

### Modifier les paramètres Django

Les paramètres principaux se trouvent dans `ecommerce/settings.py`.

## 📝 Notes

- Les images des produits sont stockées dans le dossier `media/products/`
- Le panier utilise les sessions Django
- Le paiement est simulé (paiement à la livraison)
- En production, changez `SECRET_KEY` et `DEBUG = False` dans `settings.py`

## 🐛 Dépannage

### Erreur de migration
```bash
python manage.py makemigrations
python manage.py migrate
```

### Erreur de fichiers statiques
```bash
python manage.py collectstatic
```

### Réinitialiser la base de données
```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

## 📄 Licence

Ce projet est fourni à des fins éducatives.

## 👨‍💻 Développement

Pour contribuer ou personnaliser ce projet :
1. Fork le projet
2. Créez une branche pour vos modifications
3. Testez vos changements
4. Soumettez une pull request

---

**Bon shopping ! 🛍️**

