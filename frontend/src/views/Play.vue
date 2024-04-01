<script setup lang="ts">
import Button from "@/components/atoms/Button.vue";
import GameStep from "@/components/molecules/GameStep.vue";
import LandingFrameFound from "@/components/molecules/LandingFrameFound.vue";
import { Routes } from "@/router/index";
import { useGameStore } from "@/stores/game";

const gameStore = useGameStore();
</script>

<template>
  <LandingFrameFound
    v-if="gameStore.gameState?.landing_frame != null"
    :landing-frame="gameStore.gameState.landing_frame"
    :loading="gameStore.loading"
  />
  <GameStep
    v-else-if="gameStore.gameState?.image != null"
    :image="gameStore.gameState.image"
  />
  <div v-else class="text-align-center">
    <h1>Are you ready?</h1>
    <h3>Click the button to start the game!</h3>
    <p>
      You can see a brief explanation of the game in the
      <Button type="goTo" :to="Routes.howTo" variant="inline">
        "How to play"
      </Button>
      "section."
    </p>
    <Button
      type="click"
      :on-click="() => gameStore.start()"
      :loading="gameStore.loading"
    >
      Start
    </Button>
  </div>
</template>

<style scoped>
p {
  padding-block: 12px;
}
</style>
