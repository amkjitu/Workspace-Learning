document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("submissionForm");
  const fields = [
    { id: "amount", type: "number", message: "Amount must be a number." },
    {
      id: "buyer",
      pattern: /^[a-zA-Z0-9 ]{1,20}$/,
      message:
        "Buyer name should only contain letters, spaces, and numbers, up to 20 characters.",
    },
    //{ id: "receipt_id", type: "text", message: "Receipt ID is required." },
    {
      id: "receipt_id",
      pattern: /^[^\s]+$/,
      message: "Receipt ID must not contain spaces and cannot be empty.",
    },
    //{ id: "items", type: "text", message: "Items are required." },
    {
      id: "items",
      pattern: /^[^\s]+$/,
      message: "Items must not contain spaces and cannot be empty.",
    },
    {
      id: "buyer_email",
      //pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
      pattern: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
      message: "Please enter a valid email address.",
    },
    {
      id: "note",
      validate: (value) => str_word_count(value) <= 30,
      message: "Note cannot exceed 30 words.",
    },
    {
      id: "city",
      pattern: /^[a-zA-Z ]+$/,
      message: "City should only contain letters and spaces.",
    },
    {
      id: "phone",
      pattern: /^[0-9]+$/,
      message: "Phone should only contain numbers.",
    },
    { id: "entry_by", type: "number", message: "Entry by must be a number." },
  ];

  fields.forEach((field) => {
    const input = document.getElementById(field.id);
    input.addEventListener("input", () => {
      validateField(input, field);
    });
  });

  form.addEventListener("submit", (event) => {
    let isValid = true;
    fields.forEach((field) => {
      const input = document.getElementById(field.id);
      if (!validateField(input, field)) {
        isValid = false;
      }
    });
    if (!isValid) {
      event.preventDefault();
    }
  });

  function validateField(input, field) {
    const errorElement = document.getElementById(`error_${field.id}`);
    let isValid = true;

    if (field.type === "number" && isNaN(input.value)) {
      isValid = false;
    } else if (field.pattern && !field.pattern.test(input.value)) {
      isValid = false;
    } else if (field.validate && !field.validate(input.value)) {
      isValid = false;
    }

    errorElement.textContent = isValid ? "" : field.message;
    return isValid;
  }

  function str_word_count(value) {
    return value.trim().split(/\s+/).length;
  }
});
