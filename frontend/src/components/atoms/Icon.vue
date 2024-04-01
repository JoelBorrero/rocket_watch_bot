<script setup lang="ts">
import { defineProps } from "vue";

const props = defineProps({
  icon: String,
  color: {
    type: String,
    default: "green",
  },
  size: {
    type: String,
    default: "1.5rem",
  },
});
</script>

<template>
  <font-awesome-icon :icon="'fa-solid fa-' + props.icon" color="green" />
</template>

<style scoped>
svg {
  font-size: 1.5rem;
}
</style>
