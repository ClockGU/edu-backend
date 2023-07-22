<template>
  <v-card>
    <v-card-title>
      <v-toolbar>
        <v-toolbar-title>Bewirb Dich digital, einfach und schnell auf unsere Ausbildungsberufe.</v-toolbar-title>
      </v-toolbar>
    </v-card-title>
    <v-card-text>
      <p>Wähle den Beruf aus (Mehrfachauswahl möglich):</p>
      <v-checkbox label="Verwaltungsfachangestellte/r (01.08.2024)"></v-checkbox>
      <v-checkbox label="Fachangestellte/r für Medien- und Informationsdienste (01.08.2024)"></v-checkbox>
      <p>Wir brauchen folgende Daten, um Dich von anderen zu unterscheiden:</p>
      <v-text-field label="Vorname"></v-text-field>
      <v-text-field label="Nachname"></v-text-field>
      <v-checkbox label="Sind Sie Soldat/in (Angabe freiwillig)?"></v-checkbox>
      <v-checkbox label="Liegt bei Ihnen eine körperlich, geistige oder anderweitige Einschränkung vor (Angabe freiwillig)?"></v-checkbox>
    </v-card-text>
    <v-card-actions>
      <v-btn>Zurück zur Ausbildungsseite</v-btn>
      <v-spacer/>
      <v-btn>Abschicken</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "ApplicationCard",
  data() {
    return {
      message: "Welcome to Vue!",
      s:"1"
    };
  },
};
</script>
