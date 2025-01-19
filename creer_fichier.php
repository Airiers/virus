<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $type_fichier = $_POST['type_fichier'];
    $contenu = $_POST['contenu'];

    // Définir le nom du fichier en fonction du type
    $nom_fichier = "nouveau_fichier." . $type_fichier;

    // Écrire le contenu dans le fichier
    file_put_contents($nom_fichier, $contenu);

    echo "Le fichier <strong>$nom_fichier</strong> a été créé avec succès.";
} else {
    echo "Méthode de requête non valide.";
}
?>
