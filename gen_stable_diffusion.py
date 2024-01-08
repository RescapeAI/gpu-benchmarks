import time
import argparse
t0 = time.time()


def load_pipe_sdxl():
    import torch
    from diffusers import StableDiffusionXLPipeline
    pipe = StableDiffusionXLPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16
    )
    return pipe


def load_pipe_sd21():
    from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
    import torch
    # Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
    model_id = "stabilityai/stable-diffusion-2-1"
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    return pipe


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', choices=['sdxl', 'sd21'], required=True)
    args = parser.parse_args()

    if args.model == 'sdxl':
        pipe = load_pipe_sdxl()
    elif args.model == 'sd21':
        pipe = load_pipe_sd21()

    pipe = pipe.to('cuda')

    t1 = time.time()
    print(t1 - t0)


    prompt = "a photo of an astronaut riding a horse on mars"
    image = pipe(prompt).images[0]
    
    image.save(f"astronaut_rides_horse_{args.model}.png")
    
    print(time.time() - t1)
