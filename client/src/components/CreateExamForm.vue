<script>
export default {
  data: () => ({
    topic: "",
    grade: "",
    numQuestions: "",
    numChoices: "",
    isDummyExam: true,
  }),
  props: {
    generateExam: {
      type: Function,
      required: true
    }
  },
  methods: {
    async handleGenerateExam(e) {
      const data = {
        topic: this.topic,
        grade: this.grade,
        numQuestions: this.numQuestions,
        numChoices: this.numChoices,
        isDummyExam: this.isDummyExam
      };
      await this.generateExam(e, data)
    }
  }
}
</script>

<template>
<h1>What kind of exam do you want to make?</h1>
<form>
  <!-- Topic:  -->
  <section class="form-control">
    <label for="topic">Choose the topic:</label>
    <input v-model="topic" placeholder="e.g division, Latin American history, etc.">
  </section>
  <!-- Grade:  -->
  <section class="form-control">
    <label for="grade">What grade?</label>
    <input v-model="grade" placeholder="1st grade, 12th grade, etc">
  </section>
  <!-- Number of questions:  -->
  <section class="form-control">
    <label for="numQuestions">How many questions?</label>
    <input type="number" v-model="numQuestions">
  </section>
  <!-- Number of possible answers:  -->
  <section class="form-control">
    <label for="numChoices">How many possible answers?</label>
    <input type="number" v-model="numChoices">
  </section>
  <!-- Give a dummy exam:  -->
  <section class="form-control">
    <label for="isDummyExam">Check here if you want a dummy exam to test</label>
    <input type="checkbox" v-model="isDummyExam">
  </section>
  <!-- Generate exam -->
  <button type="submit" v-on:click="handleGenerateExam">Generate exam</button>
</form>
<hr />
</template>