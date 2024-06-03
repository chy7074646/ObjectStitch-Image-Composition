import fiftyone
import fiftyone.zoo

if __name__ == '__main__':
    # dataset = fiftyone.zoo.load_zoo_dataset("open-images-v7", split="validation")
    dataset = fiftyone.zoo.load_zoo_dataset(
        "open-images-v7",
        split="train",
        label_types=["detections", "segmentations", "points"],
        classes=["Cat", "Dog"],
        max_samples=100,
        dataset_dir = "open-image-v7",
    )
    print(dataset)