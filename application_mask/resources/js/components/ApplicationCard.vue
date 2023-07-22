<template>
  <v-card>
    <v-card-title>
      <v-toolbar>
        <v-toolbar-title>Bewirb Dich digital, einfach und schnell auf unsere Ausbildungsberufe.</v-toolbar-title>
      </v-toolbar>
    </v-card-title>
    <v-card-text>
      <p>Wähle den Beruf aus (Mehrfachauswahl möglich):</p>
      <v-checkbox v-model="administrative" label="Verwaltungsfachangestellte/r (01.08.2024)" :value="true"></v-checkbox>
      <v-checkbox v-model="media" label="Fachangestellte/r für Medien- und Informationsdienste (01.08.2024)" :value="true"></v-checkbox>
      <p>Wir brauchen folgende Daten, um Dich von anderen zu unterscheiden:</p>
      <v-text-field type="input" v-model="firstname" label="Vorname"></v-text-field>
      <v-text-field type="input" v-model="lastname" label="Nachname"></v-text-field>
      <v-checkbox v-model="soldier" label="Sind Sie Soldat/in (Angabe freiwillig)?" :value="true"></v-checkbox>
      <v-checkbox v-model="disability" label="Liegt bei Ihnen eine körperlich, geistige oder anderweitige Einschränkung vor (Angabe freiwillig)?" :value="true"></v-checkbox>
    </v-card-text>
    <v-card-actions>
      <v-btn>Zurück zur Ausbildungsseite</v-btn>
      <v-spacer/>
      <v-btn @click="submitData">Abschicken</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "ApplicationCard",
  data() {
    return {
      administrative: false,
      media: false,
      firstname: "",
      lastname: "",
      soldier: false,
      disability: false,
      success: false,
      confirm: false
    };
  },
  methods: {
    submitData() {
      console.log({
      administrative: this.administrative,
      media: this.media,
      firstname: this.firstname,
      lastname: this.lastname,
      soldier: this.soldier,
      disability: this.disability,
      success: this.success,
      confirm: this.confirm
      })
    }
  }
};
</script>
