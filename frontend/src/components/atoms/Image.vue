<script setup lang="ts">
interface ImageProps {
  src: string;
  onLoad?: (event: Event) => void;
}

const props = defineProps<ImageProps>();
</script>

<template>
  <div class="img-container">
    <img :src="props.src" @load="props.onLoad" />
  </div>
</template>

<style scoped>
.img-container {
  display: grid;
  height: 100%;
}

img {
  max-width: 100%;
  max-height: 100vh;
  margin: auto;
}
</style>
