<script>
	import { onMount } from 'svelte';
	import { currentStep } from './stores';
	import Step0 from './components/Step0.svelte';
	import Step1 from './components/Step1.svelte';
	import Step2 from './components/Step2.svelte';
	import Step3 from './components/Step3.svelte';
	import Step4 from './components/Step4.svelte';
	import Step5 from './components/Step5.svelte';
	import Step6 from './components/Step6.svelte';
	import Step7 from './components/Step7.svelte';
  
	let step = 0;
	currentStep.subscribe(value => step = value);
  </script>
  
  <main>
	{#if step === 0}
	  <Step0 />
	{:else if step === 1}
	  <Step1 />
	{:else if step === 2}
	  <Step2 />
	{:else if step === 3}
	  <Step3 />
	{:else if step === 4}
	  <Step4 />
	{:else if step === 5}
	  <Step5 />
	{:else if step === 6}
	  <Step6 />
	{:else if step === 7}
	  <Step7 />
	{/if}
  </main>
  
  <style>
	main {
	  padding: 1rem;
	  max-width: 800px;
	  margin: 0 auto;
	}
  </style>
  