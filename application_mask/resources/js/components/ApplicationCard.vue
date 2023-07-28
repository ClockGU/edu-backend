<template>
  <v-card>
    <v-card-title>
      <v-toolbar>
        <v-toolbar-title>Bewirb Dich auf unsere Ausbildungsberufe - einfach und digital!</v-toolbar-title>
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
    </v-card-text>
    <v-card-title>
      <v-toolbar>
        <v-toolbar-title>Bewirb Dich auf unser Duales Studium - einfach und digital!</v-toolbar-title>
      </v-toolbar>
    </v-card-title>
    <v-card-subtitle>
      <p>Hinweis: Du benötigst die Fachhochschulreife oder allgemeine Hochschulreife (Abitur)</p>
    </v-card-subtitle>
    <v-card-text>
      <v-checkbox v-model="inspector" label="Inspektoranwärter*in - Bachelor of public Administation (Beamt*innenlaufbahn)" :value="true"></v-checkbox>
      <p>Wir brauchen folgende Daten, um Dich von anderen zu unterscheiden:</p>
      <div class="mt-4">
        <v-text-field type="input" :error-messages="firstNameErrors" @blur="v$.firstname.$touch()" v-model="firstname" label="Vorname" persistent-hint hint="Dies ist ein Pflichtfeld."></v-text-field>
        <v-text-field type="input" :error-messages="lastNameErrors" @blur="v$.lastname.$touch()" v-model="lastname" label="Nachname" persistent-hint hint="Dies ist ein Pflichtfeld."></v-text-field>
        <v-text-field type="input" :error-messages="emailErrors" @blur="v$.email.$touch()" v-model="email" label="E-Mail" persistent-hint hint="Dies ist ein Pflichtfeld."></v-text-field>
      </div>
      <v-checkbox v-model="soldier" label="Sind Sie Soldat/in (Angabe freiwillig)?" :value="true"></v-checkbox>
      <v-checkbox v-model="disability" label="Liegt bei Ihnen eine körperlich, geistige oder anderweitige Einschränkung vor (Angabe freiwillig)?" :value="true"></v-checkbox>
    </v-card-text>
    <v-card-actions>
      <v-container>
        <v-row dense>
          <v-col>
            <v-btn href="https://www.uni-frankfurt.de/103026632/Start">Zurück zur Ausbildungsseite</v-btn>
          </v-col>
          <v-col class="d-none d-lg-flex d-xl-none"><v-spacer/></v-col>
          <v-col :align="alignment">
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
            zum Eignungstest mit allen wichtigen Informationen.
          </p>
        </v-card-text>
        <v-card-actions>
            <v-btn href="https://www.uni-frankfurt.de/103026632/Start">Zurück zur Ausbildungsseite</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
import { mdiInformationOutline } from "@mdi/js";
import axios from "axios";
import { useVuelidate } from '@vuelidate/core'
import {email, helpers, required} from '@vuelidate/validators'

export default {
  name: "ApplicationCard",
  data() {
    return {
      administrative: false,
      media: false,
      inspector:false,
      firstname: null,
      lastname: null,
      email: null,
      soldier: false,
      disability: false,
      success: false,
      confirm: false,
      infoIcon: mdiInformationOutline,
      largeOrBigger: true
    };
  },
    setup() {
    return { v$: useVuelidate() };
  },
  validations() {
    return {
      firstname: {required: helpers.withMessage('Dies ist ein Pflichtfeld', required)},
      lastname: {required: helpers.withMessage('Dies ist ein Pflichtfeld', required)},
      email: {
        email: helpers.withMessage('Das ist keine korrekte Email-Adresse', email),
        required: helpers.withMessage('Dies ist ein Pflichtfeld', required)
      }
    }
  },
  computed: {
    firstNameErrors() {
      return this.v$.firstname.$errors.map( item => item.$message);
    },
    lastNameErrors() {
      return this.v$.lastname.$errors.map( item => item.$message);

    },
    emailErrors() {
      return this.v$.email.$errors.map( item => item.$message);

    },
    alignment() {
      console.log(this.largeOrBigger ? 'right' : 'left')
      return this.largeOrBigger ? 'right' : 'left';
    },
    valid(){
      if (!this.administrative && !this.media && !this.inspector){
        return false;
      }
      return !this.v$.$invalid;
    }
  },
  created() {
    const mediaQuery = window.matchMedia('(min-width: 600px)')
    const setMatchStatus = (e) => this.largeOrBigger = e.matches
    setMatchStatus(mediaQuery)
    mediaQuery.addListener(setMatchStatus)
  },
  methods: {
    async submitData() {
      if (!this.valid){
        this.confirm = false;
        return
      }
      const data = {
        administrative_appl: this.administrative,
        media_appl: this.media,
        inspector_appl: this.inspector,
        firstname: this.firstname,
        lastname: this.lastname,
        soldier: this.soldier,
        disability: this.disability,
        email: this.email
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
