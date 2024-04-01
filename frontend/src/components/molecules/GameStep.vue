<script setup lang="ts">
import { ref } from "vue";

import Button from "@/components/atoms/Button.vue";
import Image from "@/components/atoms/Image.vue";
import Loading from "@/components/atoms/Loading.vue";
import { useGameStore } from "@/stores/game";

interface GameStepProps {
  image: string;
}

const gameStore = useGameStore();
const props = defineProps<GameStepProps>();

const loading = ref(true);
const pressedClass = ref<string | null>(null);

async function play(launched: boolean) {
  loading.value = true;
  pressedClass.value = launched ? "rocket-waiting" : "anchor-waiting";
  await gameStore.play(launched);
  pressedClass.value = launched ? "rocket" : "anchor";
}
function onLoad() {
  loading.value = false;
  pressedClass.value = null;
}
</script>

<template>
  <div class="image-container">
    <Loading v-if="loading" class="loading-button" :scale="10" color="green" />
    <Image :src="props.image" :on-load="onLoad" />
  </div>
  <h3>Did the rocket launch yet?</h3>
  <div class="row">
    <Button type="click" :on-click="() => play(true)">
      <div class="row cross-axis-center">
        <p>Yes</p>
        <div class="spacer"></div>
        <h2
          class="rocket"
          :class="
            (gameStore.loading || pressedClass == 'rocket-waiting'
              ? 'animate'
              : '') + (pressedClass == 'rocket' ? ' pressed' : '')
          "
        >
          🚀
        </h2>
      </div>
    </Button>
    <div class="spacer"></div>
    <Button type="click" :on-click="() => play(false)" variant="secondary">
      <div class="row cross-axis-center">
        <p>No</p>
        <div class="spacer"></div>
        <h2
          class="anchor"
          :class="
            (gameStore.loading || pressedClass == 'anchor-waiting'
              ? 'animate'
              : '') + (pressedClass == 'anchor' ? ' pressed' : '')
          "
        >
          ⚓️
        </h2>
      </div>
    </Button>
  </div>
</template>

<style scoped>
@keyframes dropAnchor {
  100% {
    transform: translateY(12px);
  }
}
@keyframes launchRocket {
  100% {
    transform: translate3d(100vw, -100vw, 0);
  }
}
@keyframes shake-anchor {
  0%,
  100% {
    transform: rotate3d(0, 0, 1, -10deg);
  }
  50% {
    transform: rotate3d(0, 0, 1, 10deg);
  }
}
@keyframes shake-rocket {
  50% {
    transform: translate3d(8px, -8px, 0);
  }
}

h2.anchor.animate,
button:hover h2.anchor:not(.pressed) {
  animation: shake-anchor 1s infinite;
}

h2.rocket.animate,
button:hover h2.rocket:not(.pressed) {
  animation: shake-rocket 1s infinite;
}

h2.anchor.pressed {
  animation-name: dropAnchor;
  animation-duration: 2s;
  animation-fill-mode: forwards;
}

h2.rocket.pressed {
  animation-name: launchRocket;
  animation-duration: 10s;
  animation-fill-mode: forwards;
}

h3 {
  text-align: center;
}

.image-container {
  min-height: 48vw;
}

.loading-button {
  position: absolute;
  left: 0;
  right: 0;
  margin-top: 10vw;
}

.spacer {
  width: 10px;
}
</style>
