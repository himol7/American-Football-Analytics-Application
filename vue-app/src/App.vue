<template>
  <div id="app">
    <div id="nav">
      <b-jumbotron bg-variant = "info" text-variant="white" border-variant="dark">
        <template v-slot:header>American Football Analytics</template>

          <template v-slot:lead>
            Helps you determine the performance of your players during game season. Because we want your team to be the best
          </template>

          <hr class="my-4">

          <p>
            All you need is a file to start on
          </p>
      </b-jumbotron>
      </div>
      <UploadFile />
      <DisplayPhotos />
    </div>
  
</template>

<script>
import UploadFile from '@/components/UploadFile'
import DisplayPhotos from '@/components/DisplayPhotos'
export default {
  name: "App",
  components: {
    UploadFile,
    DisplayPhotos
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

</style>
