<script setup lang="ts">
import Loading from "./Loading.vue";

interface ButtonProps {
  type: "click" | "goTo";
  variant?: "inline" | "primary" | "secondary";
  onClick?: any;
  to?: string;
  loading?: boolean;
}

const props = withDefaults(defineProps<ButtonProps>(), {
  variant: "primary",
  loading: false,
});
</script>

<template>
  <button
    v-if="type == 'click'"
    :class="props.variant + (props.loading ? ' loading' : '')"
    @click="props.onClick()"
    :disabled="props.loading"
  >
    <Loading v-if="props.loading" :scale="3" color="white" />
    <slot v-else />
  </button>
  <RouterLink
    v-else-if="type === 'goTo'"
    :class="props.variant"
    :to="to ?? '#'"
    class="Button"
  >
    <slot />
  </RouterLink>
</template>

<style scoped>
a,
button {
  padding: 8px 16px;
  font-size: 16px;
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: 0.3s;
  filter: brightness(0.9);
  min-width: 72px;
}

a.inline {
  padding: 0;
  padding-inline: 4px;
  margin-inline: 4px;
  border-radius: 4px;
  height: 24px;
}

a.primary {
  border-radius: 8px;
}

a.router-link-exact-active {
  text-decoration: underline;
}

a.router-link-exact-active:hover {
  background-color: transparent;
  text-decoration: underline;
}

button.loading {
  cursor: progress;
}

button.primary {
  background-color: green;
  color: white;
}

button:hover {
  filter: brightness(1);
  transform: scale(1.05);
}
</style>
