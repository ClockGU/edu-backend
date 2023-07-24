<template>
  <v-card>
    <v-card-title>
      <v-toolbar>
        <v-toolbar-title>Bewirb Dich digital, einfach und schnell auf unsere Ausbildungsberufe.</v-toolbar-title>
      </v-toolbar>
    </v-card-title>
    <v-card-text>
      <p>
        Wähle den Beruf aus (Mehrfachauswahl möglich)
          <v-tooltip location="top" text="Mindestens eine Auswahl muss getätigt werden.">
            <template v-slot:activator="{ props }">
              <v-icon v-bind="props" :icon="infoIcon"></v-icon>
            </template>
          </v-tooltip>
        :
      </p>
      <v-checkbox v-model="administrative" label="Verwaltungsfachangestellte/r (01.08.2024)" :value="true"></v-checkbox>
      <v-checkbox v-model="media" label="Fachangestellte/r für Medien- und Informationsdienste (01.08.2024)" :value="true"></v-checkbox>
      <p>Wir brauchen folgende Daten, um Dich von anderen zu unterscheiden:</p>
      <div class="mt-4">
        <v-text-field type="input" v-model="firstname" label="Vorname" persistent-hint hint="Dies ist ein Pflichtfeld."></v-text-field>
        <v-text-field type="input" v-model="lastname" label="Nachname" persistent-hint hint="Dies ist ein Pflichtfeld."></v-text-field>
      </div>
      <v-checkbox v-model="soldier" label="Sind Sie Soldat/in (Angabe freiwillig)?" :value="true"></v-checkbox>
      <v-checkbox v-model="disability" label="Liegt bei Ihnen eine körperlich, geistige oder anderweitige Einschränkung vor (Angabe freiwillig)?" :value="true"></v-checkbox>
    </v-card-text>
    <v-card-actions>
      <v-container>
        <v-row dense>
          <v-col>
            <v-btn href="https://google.de">Zurück zur Ausbildungsseite</v-btn>
          </v-col>
          <v-col class="d-none d-lg-flex d-xl-none"><v-spacer/></v-col>
          <v-col>
            <v-btn @click="openConfirm" :disabled="!valid">Abschicken</v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-card-actions>
    <v-dialog persistent max-width="500" :model-value="confirm">
      <v-card>
        <v-card-title>
          <p> Bestatigen </p>
        </v-card-title>
        <v-card-text>
          <p>
            Mit dem Abschicken der Daten stimmst du der Verarbeitung deiner Daten
            für die Bewerbung und unsere Kommunikation mit Dir entsprechend der DSGVO zu.
          </p>
        </v-card-text>
        <v-card-actions>
            <v-btn @click="confirm=!confirm">Abbrechen</v-btn>
            <v-spacer/>
            <v-btn @click="submitData">Abschicken</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog persistent max-width="500" :model-value="success">
      <v-card>
        <v-card-title>
          <p class="text-success"> Daten erfolgreich gespeichert! </p>
        </v-card-title>
        <v-card-text>
          <h2>
            Wie sind die nächsten Schritte?
          </h2>
          <p>
            Nach der Registrierung erhältst Du eine Bestätigung per E-Mail.
            Kurz nach Ablauf der Ausschreibungsfrist senden wir Dir eine schriftliche Benachrichtigung
            zum Eignungstest allen wichtigen Informationen.
          </p>
        </v-card-text>
        <v-card-actions>
            <v-btn href="https://google.de">Zurück zur Ausbildungsseite</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
import { mdiInformationOutline } from "@mdi/js";
import axios from "axios";

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
      confirm: false,
      infoIcon: mdiInformationOutline
    };
  },
  computed: {
    valid(){
      if (!this.administrative && !this.media){
        return false;
      }
      return !(this.firstname === "" || this.lastname === "");
    }
  },
  methods: {
    async submitData() {
      if (!this.valid){
        this.confirm = false;
        return
      }
      const data = {
        administrative: this.administrative,
        media: this.media,
        firstname: this.firstname,
        lastname: this.lastname,
        soldier: this.soldier,
        disability: this.disability,
      }
      let token = document.getElementsByName("csrfmiddlewaretoken");
      axios.defaults.headers.common['X-CSRFToken'] = token[0].value;
      const response = await axios.post("/submit", data);
      if (response.status === 201){
        this.confirm = false;
        this.success = true;
      }
    },
    openConfirm() {
      this.confirm = true;
    }
  }
};
</script>
