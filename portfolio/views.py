from django.http import Http404
from django.shortcuts import render


FEATURED_PROJECTS = [
    {
        "slug": "pkcast",
        "number": "01",
        "title": "PKCast",
        "eyebrow": "Generative weather intelligence",
        "summary": "Teaching AI to read the next hour of a storm—not as one fixed answer, but as a distribution of plausible radar futures.",
        "github": "https://github.com/prerakpatel51/Pkcast",
        "live": "",
        "year": "2026",
        "icon": "cloud-lightning",
        "accent": "violet",
        "tags": ["PyTorch", "Flow Matching", "VAE", "Transformers", "HPC", "MLflow"],
        "metrics": [
            {"value": "13 → 12", "label": "Observed to forecast frames"},
            {"value": "~3.3s", "label": "Single-sample inference"},
            {"value": "Multi-GPU", "label": "Distributed training"},
        ],
        "challenge": "Weather nowcasting is both high-dimensional and uncertain. Directly forecasting full radar sequences is memory intensive, while deterministic models hide the range of plausible storm evolutions.",
        "solution": "PKCast separates representation learning from forecasting. A VAE-style autoencoder compresses SEVIR VIL radar frames to four-channel latents, then a Conditional Flow Matching model transports Gaussian noise into future latent sequences conditioned on the previous 13 frames.",
        "architecture": [
            {"title": "Prepare", "text": "Filter SEVIR events, remove incomplete sequences, split chronologically, and create 25-frame sliding windows."},
            {"title": "Compress", "text": "Train a distributed AutoencoderKL with reconstruction, KL, and PatchGAN objectives, then persist latent HDF5 datasets."},
            {"title": "Forecast", "text": "Condition a Cuboid Transformer U-Net on 13 observed latents and learn the vector field for 12 future frames."},
            {"title": "Evaluate", "text": "Decode probabilistic forecasts and stream MSE, CRPS, CSI, HSS, FAR, POD, and FSS metrics with MLflow tracking."},
        ],
        "outcomes": [
            "End-to-end research pipeline from raw SEVIR VIL events to animated probabilistic radar forecasts.",
            "Cluster-ready Slurm launchers, mixed-precision DDP training, EMA checkpoints, and early stopping.",
            "Measured inference near 3.3 seconds for a 12-frame forecast after warm-up on an NVIDIA A100.",
        ],
        "gallery": [
            {"image": "portfolio/images/projects/pkcast-ground-truth.gif", "caption": "Observed future radar sequence"},
            {"image": "portfolio/images/projects/pkcast-prediction.gif", "caption": "PKCast probabilistic prediction"},
            {"image": "portfolio/images/projects/pkcast-autoencoder-curves.png", "caption": "Autoencoder generator, discriminator, and validation training curves"},
            {"image": "portfolio/images/projects/pkcast-loss-curves.png", "caption": "Conditional Flow Matching optimization history"},
            {"image": "portfolio/images/projects/pkcast-metrics.png", "caption": "Partial-evaluation nowcasting metrics across forecast lead times"},
        ],
    },
    {
        "slug": "context-shift-xai",
        "number": "02",
        "title": "When Context Becomes Evidence",
        "eyebrow": "Vision Transformer explainability",
        "summary": "High accuracy can hide the wrong reasoning. This patch-level audit reveals when a Vision Transformer sees the object—and when it follows the background.",
        "github": "https://github.com/prerakpatel51/Context-shift-XAI-analysis",
        "live": "",
        "year": "2026",
        "icon": "scan-eye",
        "accent": "cyan",
        "tags": ["DeiT", "NICO++", "TAM", "SHAP", "Occlusion", "PyTorch"],
        "metrics": [
            {"value": "90.47%", "label": "Test accuracy"},
            {"value": "0.9064", "label": "Macro F1"},
            {"value": "44%", "label": "Context-swap flips"},
        ],
        "challenge": "Aggregate accuracy can conceal shortcut learning. A classifier may appear reliable while depending on water, grass, lighting, or seasonal textures instead of the object it claims to recognize.",
        "solution": "The project fine-tunes DeiT-Small/16 across 60 NICO++ classes and six contexts, then places transformer, gradient, perturbation, SHAP, and context-swap explanations on the same 14×14 patch grid for quantitative comparison.",
        "architecture": [
            {"title": "Train", "text": "Fine-tune an ImageNet-pretrained DeiT-Small/16 on balanced NICO++ object/context combinations."},
            {"title": "Explain", "text": "Generate token transformation, attention rollout, TAM, gradient × input, occlusion, causal patch impact, and Kernel SHAP maps."},
            {"title": "Stress test", "text": "Swap top-attributed patches between same-class images from different environments to measure context dependence."},
            {"title": "Validate", "text": "Compare methods with deletion AUC, comprehensiveness, and per-context predictive performance."},
        ],
        "outcomes": [
            "TAM achieved the strongest deletion faithfulness in the study with 0.1581 AUC (lower is better).",
            "Worst-context accuracy remained 88.92% in dim scenes, versus 92.74% in grass scenes.",
            "Top-attribution context swaps changed the prediction for 44% of same-class cross-context pairs.",
        ],
        "gallery": [
            {"image": "portfolio/images/projects/context-tam.png", "caption": "Targeted attention overlay"},
            {"image": "portfolio/images/projects/context-deletion.png", "caption": "Deletion faithfulness by XAI method"},
            {"image": "portfolio/images/projects/context-swapped.png", "caption": "Top-attribution patches replaced across visual contexts"},
            {"image": "portfolio/images/projects/context-swap-by-context.png", "caption": "Prediction-probability drop grouped by destination context"},
        ],
    },
    {
        "slug": "cross-domain-xai",
        "number": "03",
        "title": "Cross-Domain Attribution Analysis",
        "eyebrow": "Explainable AI under distribution shift",
        "summary": "Do explanations survive when the visual world changes? This study tracks model reasoning as photographs become sketches and texture gives way to shape.",
        "github": "https://github.com/prerakpatel51/xai_cross_domain_attribution_analysis",
        "live": "",
        "year": "2026",
        "icon": "blend",
        "accent": "lime",
        "tags": ["ResNet-152", "DomainNet", "Grad-CAM++", "LIME", "Integrated Gradients", "SLURM"],
        "metrics": [
            {"value": "93.63%", "label": "Best in-domain accuracy"},
            {"value": "83.02%", "label": "Best transfer accuracy"},
            {"value": "0.946", "label": "Peak XAI stability"},
        ],
        "challenge": "A model can classify familiar images well but fail when visual style changes. Heatmaps alone do not establish that its explanations remain stable, faithful, or semantically consistent out of domain.",
        "solution": "Two ResNet-152 classifiers are trained independently on photographic and sketch subsets of DomainNet. Grad-CAM, Grad-CAM++, Integrated Gradients, and LIME are evaluated across domain boundaries rather than judged only by appearance.",
        "architecture": [
            {"title": "Balance", "text": "Construct matched real and sketch splits spanning 81 classes and 29,501 training examples per domain."},
            {"title": "Train", "text": "Fine-tune independent ResNet-152 models with mixup, differential learning rates, frozen warm-up, and cosine annealing."},
            {"title": "Attribute", "text": "Generate four explanation families for every model/domain pairing using identical test samples."},
            {"title": "Measure", "text": "Score stability, insertion/deletion faithfulness, cross-domain consistency, and representation behavior."},
        ],
        "outcomes": [
            "Sketch-trained features transferred to real images at 83.02% accuracy, substantially better than the reverse direction.",
            "Grad-CAM++ produced the most stable explanations; LIME led insertion faithfulness.",
            "The analysis connects stronger sketch-to-photo transfer with shape bias and photo-to-sketch failure with texture reliance.",
        ],
        "gallery": [
            {"image": "portfolio/images/projects/xai-banana.png", "caption": "Cross-domain Grad-CAM comparison"},
            {"image": "portfolio/images/projects/xai-training.png", "caption": "Real-domain training summary"},
            {"image": "portfolio/images/projects/xai-confusion-real-sketch.png", "caption": "Real-trained model confusion matrix on sketch-domain inputs"},
            {"image": "portfolio/images/projects/xai-umap-domain.png", "caption": "UMAP view of learned representations across domains"},
        ],
    },
    {
        "slug": "satellite-segmentor",
        "number": "04",
        "title": "Satellite Image Segmentor",
        "eyebrow": "Geospatial computer vision",
        "summary": "Turning dense satellite pixels into an intelligible map—one upload, six land-cover classes, and a production-ready segmentation workflow.",
        "github": "https://github.com/prerakpatel51/satellite-image-segmentor",
        "live": "https://huggingface.co/spaces/Prerak51/satellite_image_segmentor",
        "year": "2024",
        "icon": "satellite",
        "accent": "orange",
        "tags": ["TensorFlow", "U-Net", "Gradio", "OpenCV", "Geospatial AI"],
        "metrics": [
            {"value": "6", "label": "Land-cover classes"},
            {"value": "U-Net", "label": "Segmentation backbone"},
            {"value": "Live", "label": "Hugging Face demo"},
        ],
        "challenge": "Satellite imagery contains dense, irregular boundaries and class imbalance. Useful predictions need pixel-level localization—not one label per image—and an interface accessible beyond a notebook.",
        "solution": "A U-Net variant learns semantic masks from tiled aerial imagery. Dice, Jaccard, and Focal objectives address overlap and hard examples, while a Gradio layer makes the trained model immediately testable on new images.",
        "architecture": [
            {"title": "Tile", "text": "Normalize large aerial scenes and divide them into consistent patches for training and inference."},
            {"title": "Learn", "text": "Train an encoder-decoder segmentation network with skip connections for precise spatial recovery."},
            {"title": "Optimize", "text": "Combine overlap-aware Dice/Jaccard signals with Focal Loss for challenging class boundaries."},
            {"title": "Serve", "text": "Expose upload, prediction, and mask visualization through a hosted Gradio experience."},
        ],
        "outcomes": [
            "End-to-end workflow from Kaggle aerial imagery to deployable semantic segmentation.",
            "Interactive model demo hosted on Hugging Face Spaces.",
            "Clear side-by-side visualization of the input scene and predicted class mask.",
        ],
        "gallery": [
            {"image": "portfolio/images/projects/satellite-ui.png", "caption": "Hosted segmentation interface and predicted mask"},
            {"image": "portfolio/images/projects/satellite-ui-2.png", "caption": "A second aerial scene segmented into interpretable land-cover classes"},
        ],
    },
    {
        "slug": "rainfall-forecasting",
        "number": "05",
        "title": "Hybrid Rainfall Forecasting",
        "eyebrow": "Interpretable time-series modeling",
        "summary": "Instead of forcing one model to learn every pattern, this system separates rainfall into trend, seasonality, and noise—then gives each signal the right learner.",
        "github": "https://github.com/prerakpatel51/Rainfall_prediction_using_STL_decomposition_GRU_MTGRU_",
        "live": "https://www.kaggle.com/code/patelprerak510/stl-decomposition-gru-lightgbm-rainfall-prediction",
        "year": "2024",
        "icon": "chart-no-axes-combined",
        "accent": "blue",
        "tags": ["STL", "GRU", "LightGBM", "Time Series", "TensorFlow"],
        "metrics": [
            {"value": "0.7902", "label": "Combined R²"},
            {"value": "3.335 mm", "label": "RMSE"},
            {"value": "1.385 mm", "label": "MAE"},
        ],
        "challenge": "Rainfall mixes long-term trend, recurring seasonality, and irregular weather noise. A single recurrent model has to learn all three behaviors at once and produced weak baseline performance.",
        "solution": "STL separates the observed series into interpretable components. A GRU models trend, a multi-time-scale GRU captures seasonal structure, and LightGBM handles the nonlinear remainder before predictions are recombined.",
        "architecture": [
            {"title": "Decompose", "text": "Use STL with LOESS to separate the daily series into trend, seasonality, and residual components."},
            {"title": "Specialize", "text": "Assign a GRU, multi-time-scale GRU, and LightGBM model to the component each handles best."},
            {"title": "Recombine", "text": "Aggregate component forecasts into the next-day rainfall estimate."},
            {"title": "Benchmark", "text": "Compare R², RMSE, and MAE against a direct baseline GRU."},
        ],
        "outcomes": [
            "Raised R² from 0.1618 for the baseline GRU to 0.7902 for the hybrid model.",
            "Cut RMSE from 6.6703 mm to 3.3351 mm and MAE from 2.2121 mm to 1.3846 mm.",
            "Made the modeling pipeline easier to interpret by tying each learner to a distinct time-series component.",
        ],
        "gallery": [
            {"image": "portfolio/images/projects/applypilot-hero.png", "caption": "Live ApplyPilot product: ranked job discovery and match scoring"},
        ],
    },
    {
        "slug": "applypilot-ai",
        "number": "06",
        "title": "ApplyPilot AI",
        "eyebrow": "Agentic career intelligence",
        "summary": "From job description to tailored application: coordinated AI agents find the role, explain the fit, expose the gap, and build the resume.",
        "github": "https://github.com/prerakpatel51/Apply_PilotAI",
        "live": "https://applypilot-web-production.up.railway.app/signin",
        "year": "2026",
        "icon": "route",
        "accent": "rose",
        "tags": ["LangGraph", "FastAPI", "React", "PostgreSQL", "Redis", "LaTeX"],
        "metrics": [
            {"value": "5-stage", "label": "Agent pipeline"},
            {"value": "2", "label": "LLM providers"},
            {"value": "ATS", "label": "Resume output"},
        ],
        "challenge": "Job discovery, fit analysis, and resume tailoring are fragmented across tools. Candidates repeatedly translate one master resume into role-specific evidence without a consistent workflow or traceable rationale.",
        "solution": "ApplyPilot combines a typed React workspace with a FastAPI backend and a LangGraph pipeline. It uses live search, evidence-based ranking, gap analysis, and LaTeX generation while keeping provider credentials in a bring-your-own-key model.",
        "architecture": [
            {"title": "Discover", "text": "Generate search keywords from the candidate profile and retrieve live openings through provider-backed web search."},
            {"title": "Rank", "text": "Score roles against skills, seniority, location, sponsorship, and concrete resume evidence."},
            {"title": "Tailor", "text": "Generate an ATS-focused LaTeX resume with an Overleaf-style editor and compiled PDF preview."},
            {"title": "Operate", "text": "Run agent work asynchronously with Redis/ARQ, persist records in PostgreSQL, and expose admin analytics and audit logs."},
        ],
        "outcomes": [
            "Complete search-to-application workspace with authentication, profile management, job tracking, and resume history.",
            "Provider abstraction for OpenAI and Anthropic with user-supplied session credentials and token accounting.",
            "Production-oriented safeguards including rate limiting, prompt-injection sanitization, audit logs, and encrypted credentials.",
        ],
        "gallery": [],
    },
    {
        "slug": "3d-satellite-vae",
        "number": "07",
        "title": "3D Satellite Variational Autoencoder",
        "eyebrow": "Spatiotemporal representation learning",
        "summary": "Compressing massive satellite weather volumes into a latent language that downstream forecasting models can learn faster and more efficiently.",
        "github": "https://github.com/prerakpatel51/icp_neuralnetworks_project",
        "live": "",
        "year": "2025",
        "icon": "layers-3",
        "accent": "violet",
        "tags": ["PyTorch", "3D CNN", "β-VAE", "IMERG", "Infrared", "HPC"],
        "metrics": [
            {"value": "0.00321", "label": "IMERG validation loss"},
            {"value": "12 / 16", "label": "IMERG / IR time steps"},
            {"value": "2-GPU", "label": "Cluster training"},
        ],
        "challenge": "Satellite precipitation and infrared sequences are large five-dimensional tensors. Training downstream forecasting systems directly on full-resolution volumes is expensive in memory, storage, and compute.",
        "solution": "Separate 3D convolutional β-VAE pipelines learn compact representations for IMERG and infrared sequences while preserving their temporal and spatial structure. Configuration-driven experiments run on GPU clusters with mixed precision, checkpointing, recovery, and reconstruction analysis.",
        "architecture": [
            {"title": "Ingest", "text": "Load multi-frame IMERG and infrared tensors as channel, time, height, and width volumes."},
            {"title": "Encode", "text": "Use staged Conv3D blocks, GroupNorm, SELU activations, and adaptive pooling to produce mean and log-variance fields."},
            {"title": "Sample", "text": "Apply β-weighted variational regularization and reparameterization to learn a useful stochastic latent space."},
            {"title": "Reconstruct", "text": "Decode with 3D convolution and upsampling, then compare input and reconstructed slices through PNG and GIF diagnostics."},
        ],
        "outcomes": [
            "Matched reconstructed IMERG tensors to the original temporal-spatial shape with 0.00321 validation loss.",
            "Created separate, reusable encoders for 12-step precipitation and 16-step infrared satellite sequences.",
            "Added mixed-precision training, gradient clipping, resumable checkpoints, live loss tracking, and post-training visualization for HPC experimentation.",
        ],
        "gallery": [
            {"image": "portfolio/images/projects/vae3d-imerg.png", "caption": "IMERG input and 3D VAE reconstruction analysis"},
            {"image": "portfolio/images/projects/vae3d-loss.png", "caption": "Live reconstruction and KL-loss monitoring during training"},
        ],
    },
]


PROJECT_DETAILS = {
    "pkcast": {
        "contributions": [
            "Designed the complete two-stage research pipeline: radar-frame compression followed by probabilistic latent forecasting.",
            "Built chronological SEVIR preprocessing and sliding-window generation for 13 observed and 12 future radar frames.",
            "Implemented distributed VAE and Conditional Flow Matching training with mixed precision, EMA, early stopping, and MLflow tracking.",
            "Created inference, metric-streaming, Cartopy visualization, GIF, and NPZ export workflows for repeatable evaluation.",
        ],
        "decisions": [
            {"title": "Forecast in latent space", "text": "Compressing radar frames first reduces the dimensional burden on the generative model while retaining storm structure."},
            {"title": "Model a distribution", "text": "Conditional Flow Matching represents multiple plausible futures instead of collapsing uncertainty into one deterministic frame sequence."},
            {"title": "Preserve temporal order", "text": "Chronological splits and fixed sliding windows prevent future events from leaking into training and keep evaluation operationally meaningful."},
        ],
        "evaluation": "Evaluation combines pixel error with meteorological skill. MSE and CRPS measure continuous quality and uncertainty, while CSI, pooled CSI, HSS, FAR, POD, and FSS reveal whether the model locates meaningful precipitation at multiple thresholds and spatial scales.",
        "engineering_notes": [
            "Large HDF5 sequences required streaming datasets and latent caching rather than loading the corpus into memory.",
            "Adversarial VAE training used a generator warm-up so reconstruction stabilized before the PatchGAN objective became active.",
            "Cluster execution was packaged into Slurm jobs with restartable checkpoints because long multi-GPU experiments must tolerate interruptions.",
        ],
        "next_steps": ["Increase ensemble sample count for stronger probabilistic calibration.", "Benchmark higher-order ODE solvers and additional severe-weather thresholds."],
    },
    "cross-domain-xai": {
        "contributions": [
            "Constructed balanced 81-class real and sketch DomainNet splits with matched train, validation, and test sizes.",
            "Trained independent ResNet-152 models with frozen warm-up, differential learning rates, mixup, and cosine scheduling.",
            "Implemented Grad-CAM, Grad-CAM++, Integrated Gradients, and LIME under a shared evaluation protocol.",
            "Connected prediction transfer, attribution stability, insertion/deletion faithfulness, and embedding geometry into one domain-shift analysis.",
        ],
        "decisions": [
            {"title": "Train both directions", "text": "Real-to-sketch and sketch-to-real tests separate domain difficulty from the features each training distribution encourages."},
            {"title": "Score explanations", "text": "Attribution maps are evaluated quantitatively; visual appeal alone is not treated as evidence of faithfulness."},
            {"title": "Inspect representations", "text": "t-SNE and UMAP projections help connect output behavior with the organization of features inside each network."},
        ],
        "evaluation": "The analysis measures four complementary axes: classification transfer, perturbation stability, insertion/deletion faithfulness, and cross-domain representation behavior. That combination exposes the central result: sketch training gives up some in-domain ceiling but learns shape-oriented features that travel better.",
        "engineering_notes": [
            "Every attribution method was run on consistent samples and target classes so comparisons remained meaningful.",
            "Explanation stability was separated from faithfulness—a map can look stable while highlighting features that do not drive the prediction.",
            "SLURM workflows made full model/domain/method combinations reproducible across cluster runs.",
        ],
        "next_steps": ["Extend the study to clipart, painting, quickdraw, and infograph domains.", "Evaluate concept-level and counterfactual explanations alongside pixel attribution."],
    },
    "applypilot-ai": {
        "contributions": [
            "Designed the product workflow from candidate profile and master resume through live search, ranking, gap analysis, and application assets.",
            "Built a typed React interface and FastAPI service layer covering authentication, profiles, providers, searches, jobs, resumes, usage, and administration.",
            "Orchestrated the five-stage LangGraph pipeline asynchronously with Redis and ARQ so long agent runs do not block the application.",
            "Implemented an Overleaf-style LaTeX editor with PDF compilation, downloads, version history, token accounting, and operational audit logs.",
        ],
        "decisions": [
            {"title": "Evidence before score", "text": "Every match explains aligned skills, missing signals, seniority, location, sponsorship, and the resume evidence behind its rank."},
            {"title": "Bring your own model", "text": "OpenAI and Anthropic adapters let users choose the provider while the platform centralizes orchestration and usage accounting."},
            {"title": "Jobs run off-request", "text": "Redis and ARQ isolate agent work from web requests, enabling progress tracking, retries, and predictable API latency."},
        ],
        "evaluation": "ApplyPilot is evaluated as a workflow, not just an LLM response: listing recency and active status, match-rationale completeness, resume evidence coverage, compilation success, provider token use, and end-to-end run reliability all matter.",
        "engineering_notes": [
            "Prompt-injection sanitization treats job descriptions and resumes as untrusted content before they enter agent prompts.",
            "Provider credentials, rate limits, JWT authentication, and auditability were designed as product requirements rather than later additions.",
            "The responsive workspace shifts from a desktop sidebar and split editor to a mobile bottom navigation and stacked resume preview.",
        ],
        "next_steps": ["Add human feedback loops to improve ranking weights over time.", "Expand source coverage and introduce structured application-status analytics."],
    },
    "context-shift-xai": {
        "contributions": [
            "Fine-tuned DeiT-Small/16 across 60 object classes and six annotated NICO++ environments.",
            "Unified transformer, gradient, perturbation, causal, and SHAP explanations on the same 14×14 patch grid.",
            "Designed same-class context-swap interventions to test whether top-attributed patches carry object or environmental evidence.",
            "Produced per-context performance, deletion faithfulness, comprehensiveness, layer behavior, and qualitative explanation reports.",
        ],
        "decisions": [
            {"title": "Intervene, do not only visualize", "text": "Replacing or deleting attributed patches tests whether an explanation identifies evidence the prediction actually uses."},
            {"title": "Report worst context", "text": "Aggregate accuracy is paired with environment-level results so failure in dim, water, or outdoor scenes cannot disappear in the mean."},
            {"title": "Compare method families", "text": "Attention, gradients, occlusion, causal impact, and SHAP reveal different notions of importance and different computational tradeoffs."},
        ],
        "evaluation": "TAM delivered the lowest deletion AUC in this run, while the context-swap experiment revealed that 44% of same-class cross-context pairs changed prediction. Together, those results show that a strong classifier can still rely on fragile environmental evidence.",
        "engineering_notes": [
            "Attribution outputs were normalized on a shared patch grid to prevent resolution differences from distorting comparison.",
            "Stratified evaluation kept classes and contexts represented rather than allowing dominant groups to set the result.",
            "Kernel SHAP was constrained by coalition cost, making the faithfulness/computation tradeoff visible in the report.",
        ],
        "next_steps": ["Test object masks to quantify foreground-versus-background attribution directly.", "Add context-balanced or invariant training and repeat the same audit."],
    },
    "satellite-segmentor": {
        "contributions": [
            "Prepared and tiled aerial scenes for semantic segmentation while preserving mask alignment.",
            "Developed a U-Net-style encoder-decoder with skip connections for fine land-cover boundaries.",
            "Combined Dice, Jaccard, and Focal objectives to address overlap quality and difficult minority pixels.",
            "Wrapped inference in a Gradio application and published an interactive Hugging Face Space.",
        ],
        "decisions": [
            {"title": "Segment every pixel", "text": "Environmental monitoring needs boundaries and area, not a single image label, making semantic segmentation the appropriate task."},
            {"title": "Protect spatial detail", "text": "U-Net skip connections return high-resolution encoder features to the decoder for sharper class edges."},
            {"title": "Optimize overlap", "text": "Dice and Jaccard terms align training with mask quality, while Focal Loss emphasizes hard and underrepresented pixels."},
        ],
        "evaluation": "Model quality is inspected through overlap-aware metrics and side-by-side mask visualization. The hosted interface adds a practical test: a user can upload an unseen aerial scene and immediately judge boundary quality and class consistency.",
        "engineering_notes": [
            "Large images are patchified to fit memory and reassembled without losing the mapping between imagery and masks.",
            "Color-coded outputs turn class indices into an interpretation usable by non-ML stakeholders.",
            "The Gradio layer keeps model loading and preprocessing consistent between demonstration and inference.",
        ],
        "next_steps": ["Add sliding-window blending to reduce seams on very large scenes.", "Benchmark lightweight backbones for faster CPU and edge inference."],
    },
    "rainfall-forecasting": {
        "contributions": [
            "Cleaned and resampled historical Australian weather observations into a daily forecasting series.",
            "Separated trend, seasonal structure, and remainder with STL decomposition before modeling.",
            "Built GRU, multi-time-scale GRU, and LightGBM learners specialized for different components.",
            "Benchmarked the recombined forecast against a direct GRU using R², RMSE, and MAE.",
        ],
        "decisions": [
            {"title": "Decompose before learning", "text": "Trend, seasonality, and irregular rainfall behave differently; separating them reduces the burden placed on one network."},
            {"title": "Match learner to signal", "text": "Recurrent models capture smooth temporal dependencies, while LightGBM handles nonlinear residual structure efficiently."},
            {"title": "Keep a direct baseline", "text": "The single-GRU benchmark makes the value of the hybrid design measurable rather than assumed."},
        ],
        "evaluation": "The combined forecast reached R² 0.7902, RMSE 3.3351 mm, and MAE 1.3846 mm. Against the direct GRU, that is a substantial gain in explained variance and roughly a halving of RMSE.",
        "engineering_notes": [
            "Missing observations and resampling choices were handled before decomposition to prevent artificial seasonal artifacts.",
            "Each component keeps its own training and evaluation trace so weak behavior can be diagnosed before recombination.",
            "The notebook presents exploratory plots, correlations, decomposition, component forecasts, and final benchmarking as one reproducible narrative.",
        ],
        "next_steps": ["Add probabilistic intervals for uncertainty-aware rainfall decisions.", "Test rolling-origin validation and exogenous atmospheric variables."],
    },
    "3d-satellite-vae": {
        "contributions": [
            "Developed separate 3D convolutional β-VAE pipelines for IMERG precipitation and infrared satellite volumes.",
            "Designed asymmetric spatial-temporal downsampling that preserves sequence structure while reaching a compact latent tensor.",
            "Implemented configuration-driven mixed-precision training, gradient clipping, resumable checkpoints, and best-model selection.",
            "Built live loss and reconstruction tools that export slices, animations, and post-training diagnostics.",
        ],
        "decisions": [
            {"title": "Use 3D convolutions", "text": "Treating time as a modeled dimension lets the encoder learn storm evolution rather than compressing frames independently."},
            {"title": "Control the KL tradeoff", "text": "A configurable beta balances reconstruction fidelity with a latent distribution suitable for sampling and downstream learning."},
            {"title": "Train for recovery", "text": "Timestamped experiments, optimizer-state checkpoints, and live logs make long cluster runs inspectable and restartable."},
        ],
        "evaluation": "IMERG reconstruction reached 0.00328 training loss and 0.00321 validation loss while restoring the original tensor shape. Visual slice and animation checks complement the loss by showing whether localized precipitation structure survives compression.",
        "engineering_notes": [
            "IMERG and IR use different temporal depths, so the pipelines share principles without forcing identical tensor geometry.",
            "Adaptive pooling and staged upsampling reconcile irregular 360×516 spatial dimensions with a structured latent grid.",
            "Profiling logs separate data loading, forward/backward time, and validation to expose the real GPU-training bottleneck.",
        ],
        "next_steps": ["Quantify downstream nowcasting skill from frozen versus fine-tuned latents.", "Explore vector-quantized and adversarial alternatives for sharper reconstruction."],
    },
}

for project in FEATURED_PROJECTS:
    project.update(PROJECT_DETAILS[project["slug"]])

PROJECT_ORDER = [
    "pkcast",
    "cross-domain-xai",
    "applypilot-ai",
    "context-shift-xai",
    "satellite-segmentor",
    "rainfall-forecasting",
    "3d-satellite-vae",
]
FEATURED_PROJECTS.sort(key=lambda project: PROJECT_ORDER.index(project["slug"]))
for index, project in enumerate(FEATURED_PROJECTS, start=1):
    project["number"] = f"{index:02d}"


EXPERIENCE = [
    {
        "role": "Research Assistant",
        "company": "Florida Institute of Technology",
        "date": "Apr 2026 — Present",
        "place": "Melbourne, FL",
        "focus": "Turning market narratives into measurable signals",
        "bullets": [
            "Connect news, social media, and financial language to asset-price movement through sentiment analysis and predictive modeling.",
            "Build reproducible Python and NLP pipelines for cryptocurrency and equity forecasting across regression and classification tasks.",
            "Engineer lag, momentum, and trend signals across Amazon, Google, Microsoft, and Apple to compare what each model learns—and where it fails.",
        ],
    },
    {
        "role": "Graduate Research Assistant",
        "company": "Florida Institute of Technology",
        "date": "Aug 2025 — May 2026",
        "place": "Melbourne, FL",
        "focus": "Building earlier warning from satellite and radar data",
        "bullets": [
            "Researched deep generative forecasting with Dr. Georgios C. Anagnostopoulos for satellite- and radar-based weather nowcasting.",
            "Converted 25 years of IMERG precipitation and infrared observations into repeatable spatiotemporal pipelines, cutting manual preparation by 70%.",
            "Designed VAE, diffusion, latent-diffusion, and Conditional Flow Matching systems that reduced sequence memory requirements by 35%.",
            "Scaled rare-event-aware multimodal experiments across multi-GPU and multi-node Slurm environments with checkpointing and experiment tracking.",
        ],
    },
    {
        "role": "Python Developer Intern",
        "company": "MatrixHive Technologies Pvt. Ltd.",
        "date": "Jan 2024 — Apr 2024",
        "place": "Gujarat, India",
        "focus": "Making real-time vision secure, concurrent, and scalable",
        "bullets": [
            "Engineered a secure Django API that ingested real-time RTSP camera feeds and protected the platform with end-to-end authentication.",
            "Orchestrated concurrent streams with Celery and Redis for low-latency intrusion and face-detection workloads.",
            "Trained forest-fire and smoke-detection models, then separated ingestion and inference into independently scalable services.",
        ],
    },
]


PUBLICATION = {
    "title": "Investigating Extreme Precipitation and Associated Cloud-Top Temperatures in Flash Flood Events over West Africa",
    "venue": "106th American Meteorological Society Annual Meeting",
    "year": "2026",
    "location": "Houston, Texas",
    "paper_url": "https://ams.confex.com/ams/106ANNUAL/meetingapp.cgi/Paper/473381",
    "authors": "M. Nasibi, V. Maggioni, W. Amponsah, V. Robledo, H. Vergara, P. Patel, G. C. Anagnostopoulos, D. Lamichhane, E. Nikolopoulos",
    "abstract": "When ground observations are sparse, the sky becomes the sensor. This NASA/SERVIR collaboration combines 25 years of IMERG precipitation with EUMETSAT SEVIRI infrared observations to reveal how rainfall intensity and cloud-top temperature evolve before flood and flash-flood events across West Africa.",
    "findings": [
        "All flash-flood events in the study were associated with extreme precipitation and colder cloud-top temperatures.",
        "Long-record percentile thresholds separate extremely wet, very wet, and antecedent multi-day rainfall conditions.",
        "Near-real-time precipitation and geostationary infrared data show promise for improving regional flash-flood forecasting.",
    ],
}


def _archive_projects():
    return [
        {
            "title": project["title"],
            "description": project["summary"],
            "language": project["tags"][0],
            "github": project["github"],
            "detail_url": project["slug"],
            "featured": True,
        }
        for project in FEATURED_PROJECTS
    ]


def home(request):
    return render(
        request,
        "portfolio/home.html",
        {
            "projects": FEATURED_PROJECTS,
            "experience": EXPERIENCE,
            "publication": PUBLICATION,
            "project_count": len(FEATURED_PROJECTS),
        },
    )


def project_detail(request, slug):
    project = next((item for item in FEATURED_PROJECTS if item["slug"] == slug), None)
    if project is None:
        raise Http404("Project not found")
    current_index = FEATURED_PROJECTS.index(project)
    next_project = FEATURED_PROJECTS[(current_index + 1) % len(FEATURED_PROJECTS)]
    return render(
        request,
        "portfolio/project_detail.html",
        {"project": project, "next_project": next_project},
    )


def project_archive(request):
    return render(
        request,
        "portfolio/project_archive.html",
        {"all_projects": _archive_projects(), "project_count": len(_archive_projects())},
    )
