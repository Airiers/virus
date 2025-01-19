<?php require 'header.php' ?>

<h1>Dashboard</h1>

    <!-- Bouton pour voir l'historique de Google Chrome -->
    <!--<form action="voir_historique.php" method="post">
        <button type="submit">Voir l'historique Google Chrome</button>
    </form>-->

    <!-- Formulaire pour créer un fichier -->
    <form action="creer_fichier.php" method="post">
        <h2>Créer un Fichier</h2>
        <label for="type_fichier">Type de fichier :</label>
        <select id="type_fichier" name="type_fichier">
            <option value="txt">Texte (.txt)</option>
            <option value="html">HTML (.html)</option>
            <option value="json">JSON (.json)</option>
        </select><br><br>
        <label for="contenu">Contenu du fichier :</label><br>
        <textarea id="contenu" name="contenu" rows="10" cols="50"></textarea><br><br>
        <button type="submit">Créer le fichier</button>
    </form>

    <div class="card card-primary">
              <div class="card-header">
                <h3 class="card-title"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Extensible</font></font></h3>

                <div class="card-tools">
                  <button type="button" class="btn btn-tool" data-card-widget="collapse"><i class="fas fa-minus"></i>
                  </button>
                </div>
                <!-- /.card-tools -->
              </div>
              <!-- /.card-header -->
              <div class="card-body" style="display: block;"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
                Le corps de la carte
              </font></font></div>
              <!-- /.card-body -->
            </div>

<?php require 'footer.php' ?>