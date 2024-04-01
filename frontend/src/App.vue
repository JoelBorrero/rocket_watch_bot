<script setup lang="ts">
import { RouterView } from "vue-router";

import Button from "@/components/atoms/Button.vue";
import { Routes } from "@/router/index";
</script>

<template>
  <div class="column">
    <header>
      <nav class="row">
        <Button type="goTo" :to="Routes.play">Home</Button>
        <Button type="goTo" :to="Routes.howTo">About</Button>
      </nav>
      <img
        alt="logo"
        class="logo"
        src="@/assets/rocket.png"
        width="72"
        height="72"
      />
    </header>
    <RouterView />
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
  padding-bottom: 24px;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
  border-radius: 10%;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>

<style>
#app {
  display: flex;
}

.row {
  display: flex;
  justify-content: center;
}

.col {
  margin: 0 1rem;
}

.row.cross-axis-center {
  align-items: center;
}

.text-align-center {
  text-align: center;
}
</style>
