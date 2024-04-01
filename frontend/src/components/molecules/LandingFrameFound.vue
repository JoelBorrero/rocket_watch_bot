<script setup lang="ts">
import Button from "@/components/atoms/Button.vue";
import { useGameStore } from "@/stores/game";

interface LandingFrameFoundProps {
  landingFrame: number;
  loading: boolean;
}

function playAgain() {
  useGameStore().reset();
}

const props = defineProps<LandingFrameFoundProps>();
</script>

<template>
  <div class="text-align-center">
    <h1>Yay!</h1>
    <h2>You found the landing frame!</h2>
    <p>
      Thanks to your skills, we know that the rocket landed on the frame
      <strong>{{ props.landingFrame }}</strong>
      .
    </p>
    <br />
    <Button type="click" :on-click="() => playAgain()" :loading="props.loading">
      Play again
    </Button>
  </div>
</template>
