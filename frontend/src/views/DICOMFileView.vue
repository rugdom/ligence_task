<template>
  <div class="container">
    <div class="row">
      <div class="col col-sm-10">
        <h1 class="mt-5 mb-3">DICOM Files:</h1>
        
        <div>
          <ul class="list-group">
            <li :class="(selected == file.pk)? 'list-group-item list-group-item-success':'list-group-item'" v-for="file in files" :key="file.pk">
              <a class="text-decoration-none" :href="file.file">{{ file.file }}</a>
              <a class="text-decoration-none link-button float-end px-3" @click="showFileData(file.pk)">View</a>
            </li>
          </ul>
        </div>

      </div>
    </div>

    <div class="row">
      <div class="col col-sm-10">
        <div v-if="Object.keys(file_data).length">
          <div class="float-end mt-5">
            <a class="text-decoration-none link-button" @click="closeTable">Close</a>
          </div>

          <table class="table table-striped">
            <thead>
              <tr class="table-success">
                <th scope="col">Tag</th>
                <th scope="col">Value</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(val, key) in file_data" :key="key">
                <td>{{ key }}</td>
                <td>{{ val }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
const API_URL = 'http://127.0.0.1:8000/api/'
import axios from 'axios'

export default {
  name: 'DICOMFiles',
  data () {
    return {
      files: [],
      file_data: [],
      selected: ""
    }
  },
  mounted () {
    this.getFiles()
  },
  methods: {
    getFiles() {
      axios({
        method: 'get',
        url: API_URL + 'dicomfiles/',
      }).then(response => {
        this.files = response.data
      }).catch((error) => {
          console.log(error)
      })
    },
    showFileData(file_id) {
      axios({
        method: 'get',
        url: API_URL + 'dicomfiles/' + file_id + '/',
      }).then(response => {
        this.file_data = response.data.file_data
        this.selected = file_id
      }).catch((error) => {
          console.log(error)
      })
    },
    closeTable() {
      this.file_data = []
      this.selected = ""
    }
  }
}
</script>

<style>
.link-button {
  cursor: pointer;
}
tr {
  width: 100%;
  display: inline-table;
  table-layout: fixed;
}
tbody{
  height: 450px;
  overflow: auto;
  display: block;
}
</style>