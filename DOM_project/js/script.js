document.addEventListener('DOMContentLoaded', () => {
  const totalPriceElement = document.querySelector('.total');
  const productWrappers = document.querySelectorAll('.list-products > .card-body');

  const parsePrice = (text) => Number(text.replace('$', '').trim()) || 0;

  const updateTotal = () => {
    let total = 0;
    document.querySelectorAll('.list-products > .card-body').forEach((wrapper) => {
      const priceEl = wrapper.querySelector('.unit-price');
      const qtyEl = wrapper.querySelector('.quantity');
      if (!priceEl || !qtyEl) return;
      const price = parsePrice(priceEl.textContent);
      const quantity = Number(qtyEl.textContent) || 0;
      total += price * quantity;
    });
    totalPriceElement.textContent = `${total} $`;
  };

  const changeQuantity = (qtyEl, delta) => {
    const current = Number(qtyEl.textContent) || 0;
    const next = Math.max(0, current + delta);
    qtyEl.textContent = next;
    updateTotal();
  };

  const bindProductCard = (wrapper) => {
    const plusBtn = wrapper.querySelector('.fa-plus-circle');
    const minusBtn = wrapper.querySelector('.fa-minus-circle');
    const trashBtn = wrapper.querySelector('.fa-trash-alt');
    const heartBtn = wrapper.querySelector('.fa-heart');
    const qtyEl = wrapper.querySelector('.quantity');

    if (plusBtn) {
      plusBtn.addEventListener('click', () => changeQuantity(qtyEl, 1));
    }

    if (minusBtn) {
      minusBtn.addEventListener('click', () => changeQuantity(qtyEl, -1));
    }

    if (trashBtn) {
      trashBtn.addEventListener('click', () => {
        wrapper.remove();
        updateTotal();
      });
    }

    if (heartBtn) {
      heartBtn.addEventListener('click', () => {
        heartBtn.classList.toggle('liked');
      });
    }
  };

  productWrappers.forEach(bindProductCard);
  updateTotal();
});
