# hj
#  Hugging Face Trainer setup and run

# src/ner/trainer_setup.py

from transformers import TrainingArguments, Trainer, DataCollatorForTokenClassification

def setup_trainer(model, tokenizer, tokenized_dataset, output_dir="./ner-model", epochs=5):
    args = TrainingArguments(
        output_dir=output_dir,
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=epochs,
        weight_decay=0.01,
    )

    data_collator = DataCollatorForTokenClassification(tokenizer)

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=tokenized_dataset["train"],
        eval_dataset=tokenized_dataset["test"],
        tokenizer=tokenizer,
        data_collator=data_collator,
    )

    return trainer
