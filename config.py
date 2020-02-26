import json

data = {
    "embeddings": [
        {
            "tensorPath": "oss_data/face_tensor.bytes",
            "tensorShape": [
                675,
                128
            ],
            "metadataPath": "oss_data/face_labels_2.tsv",
            "tensorName": "VisualFace",
            "sprite": {
                "imagePath": "oss_data/face_sprites_2.png",
                "singleImageDim": [
                    112,
                    112
                ]
            }
        }
    ],
    "modelCheckpointPath": "Visual Vector Embedding"
}

with open('./oss_data/oss_face_config.json', 'w') as fp:
    json.dump(data, fp)