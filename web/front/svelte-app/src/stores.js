import { writable } from 'svelte/store';

export const currentStep = writable(0);
export const tripDetails = writable({
  role: '',
  origin: '',
  destination: '',
  date: '',
  timeRange: { from: '', to: '' },
  tripType: '',
  price: 0,
  car: null,
  additionalInfo: ''
});
