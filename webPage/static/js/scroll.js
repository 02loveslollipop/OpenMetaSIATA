const heroSection = document.querySelector('.herocontent2');
const heroTitle = document.querySelector('.hero h1');
const heroText = document.querySelector('.hero p');

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      heroSection.classList.add('animated');
    } else {
      heroSection.classList.remove('animated');
    }
  });
});

observer.observe(heroSection);
