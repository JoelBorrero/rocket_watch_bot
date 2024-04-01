<script setup lang="ts">
import Button from "@/components/atoms/Button.vue";
import Icon from "@/components/atoms/Icon.vue";
import SectionItem from "@/components/atoms/SectionItem.vue";
import { Icons } from "@/fontAwesome";
import { Routes } from "@/router/index.ts";
</script>

<template>
  <div class="text-align-center">
    <h3>Welcome to the</h3>
    <h1 class="green">Rocket Watch Bot 🚀</h1>
  </div>
  <SectionItem>
    <template #icon>
      <Icon :icon="Icons.question" />
    </template>
    <template #heading>What to do?</template>
    In this exciting game, you'll get the chance to test your observation skills
    and guess when a rocket is launched during a thrilling video sequence. Your
    participation will help us pinpoint the exact moment of the rocket launch!
  </SectionItem>

  <SectionItem>
    <template #icon>
      <Icon :icon="Icons.play" />
    </template>
    <template #heading>How to play?</template>
    <ol>
      <li>The bot will present you with images from a rocket launch video.</li>
      <li>
        Your task is to carefully observe each image and determine whether the
        rocket has launched yet.
      </li>
      <li>
        Simply reply with "yes" if you believe the rocket has launched or "no"
        if it hasn't.
      </li>
    </ol>
  </SectionItem>

  <SectionItem>
    <template #icon>
      <Icon :icon="Icons.handshake" />
    </template>
    <template #heading>Your Contribution</template>
    By providing your input, you'll assist us in identifying the frame where the
    rocket takes off. Your guesses will be crucial in solving this intriguing
    challenge!
  </SectionItem>

  <SectionItem>
    <template #icon>
      <Icon :icon="Icons.filter" />
    </template>
    <template #heading>Expected Output</template>
    At the end of the game, the bot will reveal the date it has guessed for the
    rocket launch event based on your responses.
  </SectionItem>

  <SectionItem>
    <template #icon>
      <Icon :icon="Icons.angleRight" />
    </template>
    <template #heading>Let's do it!</template>
    Let's embark on this journey together and unravel the mysteries of space
    exploration! Feel free to ask any questions or seek assistance along the
    way. Have fun!
  </SectionItem>
  <div class="text-align-center" style="margin-block: 12px">
    <Button type="goTo" :to="Routes.play"> Go! </Button>
  </div>
</template>
