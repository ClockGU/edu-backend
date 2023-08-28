<template>
    <v-dialog persistent max-width="500" :model-value="show">
      <v-card>
        <v-card-title>
          <p class="text-amber"> Die Bewerbungsfrist ist beendet. </p>
        </v-card-title>
        <v-card-text>
          <h2>
            Wie sind die nächsten Schritte?
          </h2>
          <p>
            Die Frist für die diesjährige Bewerbungsrunde ist beendet.
          </p>
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