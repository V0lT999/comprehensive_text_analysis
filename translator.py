import os
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

directory = "facebook"
model_name = "mbart-large-50-many-to-many-mmt"
default_model_name = f'{directory}/model/{model_name}'
default_tokenizer_name = f'{directory}/tokenizer/{model_name}'

model_name = f'{directory}/{model_name}'


if not os.path.exists(default_model_name):
    model = MBartForConditionalGeneration.from_pretrained(model_name)
    if not os.path.exists(directory + '/model'):
        os.makedirs(directory + '/model')
    model.save_pretrained(save_directory=default_model_name)
else:
    model = MBartForConditionalGeneration.from_pretrained(default_model_name)


if not os.path.exists(default_tokenizer_name):
    tokenizer = MBart50TokenizerFast.from_pretrained(model_name, src_lang="en_XX")
    if not os.path.exists(directory + '/model'):
        os.makedirs(directory + '/tokenizer')
    tokenizer.save_pretrained(save_directory=default_tokenizer_name)
else:
    tokenizer = MBart50TokenizerFast.from_pretrained(default_tokenizer_name, src_lang="en_XX")


def translate(text: str):
    phrases = text.split('.')[:-1]
    translation = list()
    for phrase in phrases:
        model_inputs = tokenizer(phrase, return_tensors="pt")
        generated_tokens = model.generate(
            **model_inputs,
            forced_bos_token_id=tokenizer.lang_code_to_id["ru_RU"]
        )
        translation.extend(tokenizer.batch_decode(generated_tokens, skip_special_tokens=True))
    return ". ".join(translation)


if __name__ == '__main__':
    print(
        translate(
            text='''We determine policy subject land mouth. Blood blue black player.
                    Put play class. Raise education lawyer debate accept. 
                    Laugh minute alone for nor short four.'''
        )
    )
