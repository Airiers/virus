<?php
// Chemin complet du fichier SQLite de l'historique de Chrome
$dbPath = 'C:\\Users\\willi\\AppData\\Local\\CCleaner Browser\\User Data\\Default\\History';

// Vérifier si le fichier existe
if (file_exists($dbPath)) {
    // Connexion à la base de données SQLite
    $db = new SQLite3($dbPath);

    // Requête pour obtenir l'historique
    $results = $db->query('SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC');

    // Affichage des résultats
    echo "<h1>Historique Google Chrome</h1>";
    echo "<table border='1'>";
    echo "<tr><th>URL</th><th>Titre</th><th>Dernière visite</th></tr>";
    while ($row = $results->fetchArray()) {
        echo "<tr><td>{$row['url']}</td><td>{$row['title']}</td><td>{$row['last_visit_time']}</td></tr>";
    }
    echo "</table>";

    // Fermeture de la connexion
    $db->close();
} else {
    echo "Le fichier d'historique de Chrome n'a pas été trouvé.";
}
?>
