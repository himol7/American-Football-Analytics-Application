<template>
  <div id="app">
    <div id="nav">
      <UploadFile />
      <DisplayPhotos />
    </div>
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
