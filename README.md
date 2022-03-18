# aws-lambda-docker

> AWS의 Lambda 환경 구성을 위한  유용한 Dockerfile 모음집 (python 3.8 기준)

## Preliminary Setup

- Docker 설치
- AWS CLI 설치
- IAM 사용자 생성 및 등록(aws configure)


## Project Structure

```
- Dockerfile: 컨테이너를 구성시켜줄 파일
- app.py: 람다 함수 핸들러 
- requirements.txt: 필요한 Python 라이브러리
```

## Deployment

> 우선 ECS > ECR로 들어가서 레포지터리를 생성해줍니다.

```bash
// ECR auth: 
aws configure 
aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin [Your-AWS-ID].dkr.ecr.ap-northeast-2.amazonaws.com

// run
docker run -p 9000:8080 container-name:latest 

// build
docker build -t container-name .                    
 
// Register
docker tag container-name:latest 867962454909.dkr.ecr.ap-northeast-2.amazonaws.com/container-name:latest      

docker push [Your-AWS-ID].dkr.ecr.ap-northeast-2.amazonaws.com/container-name:latest

```

## Update Table

| 이름 | 링크 |  업데이트 | 
| :------- | :------- | :-------: |
| **Opencv 환경** | https://github.com/sanghoho/aws-lambda-docker/tree/main/opencv | 2022-03-16 |
