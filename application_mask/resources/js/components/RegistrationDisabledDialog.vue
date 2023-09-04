<template>
    <v-dialog persistent max-width="500" :model-value="show">
      <v-card>
        <v-card-title>
          <p class="text-"> Die Bewerbungsfrist ist beendet. </p>
        </v-card-title>
        <v-card-text>
          <h2>
            Ooops was ist hier passiert?
          </h2>
          <div class="mt-4 mb-4">
            <p>
              Liebe Bewerbende,
            </p>
          </div>
          <span>
            leider ist die Bewerbungsfrist für unsere Ausschreibung abgelaufen. Deine Bewerbung können wir somit nicht mehr berücksichtigen.
            Informiere Dich über Neuigkeiten gerne immer auf unserer Ausbildungsseite.
          </span>
          <div class="mt-4">
            <p>
              Das Ausbildungsteam
            </p>
          </div>
        </v-card-text>
        <v-card-actions>
            <v-btn href="https://www.uni-frankfurt.de/103026632/Start">Zurück zur Ausbildungsseite</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
</template>

<script>

export default {
  name: "RegistrationDisabledDialog",
    props:{
    booleanInteger: {
      type: Number,
      required: true
    }
  },
  computed:{
    show() {
      console.log(Boolean(this.booleanInteger));
      return Boolean(this.booleanInteger);
    }
  }
}
</script>

<style scoped>

</style>