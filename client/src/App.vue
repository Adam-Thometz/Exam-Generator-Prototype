<script>
import './assets/main.css'
import CreateExamForm from './components/CreateExamForm.vue';

import axios from "axios"

const BASE_URL = "http://localhost:3001"

export default {
  components: {
    CreateExamForm
  },
  data: () => ({
    data: {},
    exam: "",
  }),
  methods: {
    async generateExam(e, data) {
      e.preventDefault();
      this.data = data;
      const examDisplay = document.getElementById('exam');
      examDisplay.innerText = "Loading..."
      
      if ((!data.topic || !data.grade || !data.numQuestions || !data.numChoices) && !data.isDummyExam) {
        examDisplay.innerText = "Please fill out all the fields or select that you want a dummy test"
        return
      }

      const response = await axios.post(`${BASE_URL}/create`, {
        data,
        headers: { 'Content-Type': 'application/json' },
        responseType: 'text',
      })
      this.exam = response.data
      const examData = this.exam.split("\n")
      this.createExamHTML(examData, examDisplay)
    },
    createExamHTML(data, display) {
      display.innerText = ""

      for (let line of data) {
        const lineToAppend = document.createElement('p')
        lineToAppend.innerText = line
        display.append(lineToAppend)
        if (line.slice(0, 7) === "Correct") {
          const lineBreak = document.createElement('br')
          display.append(lineBreak)
        }
      }
      
      this.createDownloadBtn(display)
    },
    createDownloadBtn(display) {
      const downloadBtn = document.createElement('button')
      downloadBtn.innerText = "Download exam"
      downloadBtn.addEventListener('click', async () => {
        const { isDummyExam, grade, topic } = this.data
        const fileName = `${
          isDummyExam ? 'beginner' : grade.replaceAll(" ", "-")
        }-${
          isDummyExam ? 'python' : topic.replaceAll(" ", "-")
        }-exam.txt`
        const download = document.createElement('a')
        download.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(this.exam))
        download.setAttribute('download', fileName)

        download.style.display = 'none'
        document.body.appendChild(download)

        download.click()
        document.body.removeChild(download)
      })
      display.append(downloadBtn)
    },
  },
}
</script>

<template>
  <CreateExamForm :generateExam="generateExam" />
  <div id="exam"></div>
</template>

<style scoped>

</style>
