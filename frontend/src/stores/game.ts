import { ref } from "vue";
import { defineStore } from "pinia";

import Api, { type State } from "@/api";

export const useGameStore = defineStore("game", () => {
  const loading = ref(false);
  const gameState = ref<State | null>(null);

  async function play(launched: boolean) {
    loading.value = true;
    const response = await Api.play(launched, gameState.value!);
    console.log(response);
    gameState.value = response;
    loading.value = false;
  }

  async function reset() {
    loading.value = true;
    await new Promise((resolve) => setTimeout(resolve, 1000));
    gameState.value = null;
    loading.value = false;
  }

  async function start() {
    loading.value = true;
    const response = await Api.start();
    gameState.value = response;
    loading.value = false;
  }

  return { gameState, loading, play, reset, start };
});
